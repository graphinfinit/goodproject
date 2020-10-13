from django.shortcuts import render


from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


from django.core.mail import send_mail


from django.conf import settings

from . import signals






"""
python -m smtpd -n -c DebuggingServer localhost:1025
       
def activate_user(request):
    username = request.POST['username']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        
    else:
        pass
    """

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
        """Отправляет email и сохраняет пользователя неактивным (signals/postsave)"""

        form.save()

        subject = "NAME"
        message_link = "LINK"
        num_letter = send_mail(
            'Hello,'.format(subject),
            'Follow the link for registration {}'.format(message_link),
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def good_scum(request):
    return render(request,'registration/success_reg.html')
