
from django.contrib import admin
from .models import *




class Product_in_BasketInline(admin.TabularInline):
    model = Product_in_Basket
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'status','created','updated','phone']
    inlines = [Product_in_BasketInline]
    
    class Meta:
        model = Order
        
        
        
        


class CartAdmin(admin.ModelAdmin):
    list_display = ['session_key','product','number']

    class Meta:
        model = Cart
        
        

admin.site.register(Shop_product) 
admin.site.register(Product_in_Basket)
admin.site.register(Order, OrderAdmin)
admin.site.register(Status)
admin.site.register(Image_Product)

admin.site.register(Cart, CartAdmin)