from django.urls import path , re_path
from . import views

urlpatterns = [
    path(r'$', views.MyRegisterFormView.as_view(), name = 'registration'),
    path(r'success', views.good_scum, name = 'success')
    ]

