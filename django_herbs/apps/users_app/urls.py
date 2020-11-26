from django.urls import path, re_path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'$', views.MyRegisterFormView.as_view(), name='registration'),


    path(r'success', views.good_scum, name='success'),
    path(r'edit_profile', views.edit_profile, name='edit_profile'),
    re_path(r'activate_user/(?P<user_id>\w+)', views.activate_user, name='activate_user'),



    path(r'^password-reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')


]





