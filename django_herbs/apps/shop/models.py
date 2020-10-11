from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Shop_product(models.Model):
    id_product = models.IntegerField('Код товара')
    name_product = models.CharField('Название товара',max_length = 50)
    text_product = models.TextField('Описание товара')
    price_product = models.PositiveIntegerField('Цена в рублях')
    quantity_product = models.PositiveIntegerField('Количество')
   
    def __str__(self):
        return '%s' % (self.name_product)
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Image_Product(models.Model):
    product = models.OneToOneField(Shop_product, on_delete=models.CASCADE,
        primary_key=True)
    image = models.ImageField(upload_to = 'img/')  # путь относительно папки  Media  в настройках
    is_active = models.BooleanField(default = True)
    def __str__(self):
        return '%s %s' % (self.product, self.image )
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'



class Status(models.Model):
    status_name = models.CharField(max_length = 10)
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'    
    def __str__(self):
        return '%s %s' % (self.status_name, self.id ) # id заказа 


class Order(models.Model):
    name = models.ForeignKey(User, on_delete = models.CASCADE, blank=True)
    email = models.EmailField()
    phone = models.CharField('Номер телефона', max_length = 30)
    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    comment = models.TextField('Комментарий')
    adress_dostavka = models.CharField('Адрес доставки', max_length = 128)
    status = models.ForeignKey(Status, on_delete= models.CASCADE, default = None)
    
    def __str__(self):
        return '%s' % (self.id) # id заказа
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
  
  
class Product_in_Basket(models.Model):
    basket = models.ForeignKey(Order, on_delete= models.CASCADE)
    product = models.ForeignKey(Shop_product, on_delete= models.CASCADE)
    number = models.IntegerField(default = 1)
    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    price = models.PositiveIntegerField(default = 1)
    total_price = models.PositiveIntegerField(default = 1)
    
    
    def __str__(self):
        return '%s' % (self.basket) # id заказа
    
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товар в корзине'
    
    def save(self,*args,**kwargs):
        price_product = self.product.price_product
        self.price_product = price_product
        self.total_price = self.number * price_product
        
        super(Product_in_Basket, self).save(*args,**kwargs)
 
 

class Cart(models.Model):

    session_key = models.CharField(max_length = 128, default = None)
    product = models.ForeignKey(Shop_product, on_delete= models.CASCADE, null = True)
    number = models.PositiveIntegerField(default = 1, null = True)
    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)



    def __str__(self):
        return '%s id %s' % (self.session_key, self.id ) # id заказа

    class Meta:
        verbose_name = 'Продукт (Сессионная корзина) '
        verbose_name_plural = 'Продукты (Сессионная корзина) '



    


