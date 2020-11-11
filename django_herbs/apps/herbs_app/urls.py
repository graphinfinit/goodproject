from django.urls import path , re_path

from . import views


urlpatterns = [
    path('', views.herbs_app_main, name = 'herbs_app'),
    path('new/', views.new_items, name = 'new_items'),
    re_path(r'^items/(?P<herb_id>\d+)$', views.herb_id_info, name='herb_info'),
    path('search/', views.search_title, name = 'search_title'),
    re_path(r'^items/(?P<herb_id>\d+)/leave_comment', views.leave_comment, name='leave_comment'),
    path('about/', views.all_info, name = 'about') ,
    path('leave_article/', views.leave_aricle, name='leave_article'),
]


