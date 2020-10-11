from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


from django.contrib.auth.forms import UserCreationForm
#A view that displays a form. On error, redisplays the form with validation errors; on success, redirects to a new URL.




"""

from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
    )
    
    
    
    
    Определите функцию для активации пользователя (т. е. def активировать (запрос))
        Настройте в url.py маршрут к этой функции (т. е. /activate/)
    Создание формы для регистрации пользователя
    Создать функции для создания пользователей
        При создании пользователя установите для поля 'is_active' значение 0.
        В той же функции Отправить email со ссылкой внутри, эта ссылка должна иметь цель в качестве настроенного маршрута

    
    """

def activate_user(request):
    username = request.POST['username']
    user = authenticate(request, username=username, password=password)



    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...



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
        """Отправляем email и сохраняем пользователя неактивным"""

        form.is_active = False
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)




def good_scum(request):
    return render(request,'registration/success_reg.html')
