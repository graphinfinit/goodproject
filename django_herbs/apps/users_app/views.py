from django.contrib.auth.models import User

from django_herbs.settings import DOMEN


from django.shortcuts import render, HttpResponse
from django import forms


from django.contrib.auth.forms import UserCreationForm, PasswordResetForm


from django.views.generic.edit import FormView
from django.core.exceptions import ValidationError


from django.conf import settings
from . import signals
from .tasks import send_asyncio
from .encript import *


def activate_user(request, user_id):
    '''Активация пользователя по его id.'''
    user_id = str(decripte(ciphertext = user_id , secret_key=secret_key))
    user_object = User.objects.get(id = user_id)
    if user_object is not None:
        user_object.is_active = True
        user_object.save(update_fields = ['is_active'])

        return render(request, 'registration/success_reg.html')
    else:
        raise ValidationError("Ошибка активации! Проверьте целостность ссылки")


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_active = False

        if User.objects.filter(email=self.cleaned_data["email"]).exists():
            raise ValidationError("Такой email уже существует. Возможно вы уже были зарегестрированы")
        else:
            if commit:
                user.save()
            return user

class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/users_q/success"
    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        """Отправляет email (celery) и сохраняет пользователя неактивным """
        form.save()
        username = form.cleaned_data['username']
        from_email = 'graphinfinit@gmail.com'
        to_email = form.cleaned_data['email']

        user_id = User.objects.get(username=username).id
        e_user_id = encript(secret_key=secret_key, text=str(user_id))
        link = 'http://'+ DOMEN + "/users_q/activate_user/"+ str(e_user_id)

        # см. tasks.py
        send_asyncio.delay(from_email=from_email, to_email=to_email, subject=username, link=link)
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)




def good_scum(request):
    return render(request,'registration/presuccess_reg.html')

def edit_profile(request):

    return render(request, 'profile/edit_profile.html')




