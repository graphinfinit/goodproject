from django.shortcuts import render


from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


from django.conf import settings

from . import signals


from .tasks import send_asyncio






'''
def activate_user(request, id):
    user_object = get_user(id)

    if user is not None:
        login(request, user)
        
    else:
        pass

'''





class UserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/users_q/success"
    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        """Отправляет email (celery) и сохраняет пользователя неактивным (signals/postsave)"""

        form.save()

        # см. tasks.py
        send_asyncio.delay()


        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def good_scum(request):
    return render(request,'registration/success_reg.html')


def edit_profile(request):
    return render(request, 'profile/edit_profile.html')




