from django.urls import path , re_path

from . import views


urlpatterns = [
    path('',views.shop_product, name = 'shop_product'),
    re_path(r'^(?P<product_id>\d+)', views.shop_product_id, name='shop_product'),
    path('add_order',views.add_order, name = 'add_order'),
    path('show_orders',views.show_orders, name = 'show_orders'),

]


