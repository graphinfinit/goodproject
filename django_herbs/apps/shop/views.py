from django.shortcuts import render, redirect, HttpResponse
from django.http import *

from .models import *
# Create your views here.
from django.http import JsonResponse
from django.middleware import csrf

from django.contrib.auth.decorators import login_required

from .forms  import CartForm, OrderForm

from django.core.exceptions import ObjectDoesNotExist


@login_required
def shop_product(request):
    '''Рендерит все продукты по id картинки
    Нужно добавить красивую пагинацию js
    '''
    product_list = Shop_product.objects.all()
    image_list = Image_Product.objects.all()
    data = {"product_list":product_list, "image_list":image_list}

    return render(request,'shop/shop_main.html', context = data)

@login_required
def shop_product_id(request, product_id):
    '''Отображает карточку конкретного товара с формой для отправки в сессионную корзину.
    При Post запросе сохраняет форму в сессионную базу,если товара в ней нет, или увеличивает количество товара'''

    if request.method == 'POST':
        cartform = CartForm(data=request.POST)
        if cartform.is_valid():
            product_set = Shop_product.objects.get(id=product_id)

            try:
                cart_set = Cart.objects.get(session_key= request.POST["session_key"], product = product_set)
                cart_set.number = int(request.POST["number"]) + int(cart_set.number)
                cart_set.save()
                return redirect(shop_product)
            except ObjectDoesNotExist:
                cartform.save()
                return redirect(shop_product)

    else:
        product_set = Shop_product.objects.get(id=product_id)
        image = Image_Product.objects.get(product=product_set)

        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()

        cartform = CartForm({"session_key":session_key,"product": product_set})

        return render(request, 'shop/shop_product.html', context={'product_set': product_set,
                                                                   'cartform': cartform, "image": image})


@login_required
def add_order(request):
    '''
    Обзор товаров в корзине.
    Заполнение формы заказа.
    Удаление сессионной корзины в случае подтвеждения заказа и перенаправление ко всем заказам и оплате.


    :param request:
    :return:
    '''


    if request.method == "POST":
        order_form = OrderForm(data=request.POST)
        if order_form.is_valid():
            print(order_form)
            order = order_form.save(commit=False)
            order.name = request.user
            order.status = Status.objects.get(id = 1)# СтатусP:Оформлен
            order.save()
            # Добавление товаров из сессии в заказ
            cart_set = Cart.objects.filter(session_key=request.session.session_key)
            for cart in cart_set:
                orderon = Product_in_Basket.objects.get_or_create(
                    basket= order,
                    product = cart.product,
                    price = cart.product.price_product,
                    number = cart.number
                )
            cart_set.delete()

            order.save() # для обновлния поля общей суммы в методе save

            return redirect(show_orders)
        else:
            return HttpResponseBadRequest('<h1>Форма не прошла валидацию!Проверьте правильность введенных данных</h1><br>')

    else:
        cart_set = Cart.objects.filter(session_key= request.session.session_key)
        lock = cart_set.count()
        if lock == 0:
            return render(request,'shop/null_cart_error.html')
        else:
            shop_product = Shop_product.objects.all()
            order_form = OrderForm()
            return render(request, 'shop/order.html', context={'order_form': order_form, 'cart_set': cart_set,
                                                               'shop_product':shop_product})

@login_required
def show_orders(request):
    '''Показывает все заказы пользователя и по POST запросу:
     1) удаляет заказ
     2)перенаправляет к форме оплаты
     '''

    if request.method == "POST":
        if request.POST['order_id'][:3] == 'pay':
            print(request.POST['order_id'][3:])
            order_id = request.POST['order_id'][4:]

            return redirect('/shop/pay/'+ str(order_id))

        else:
            order_id = request.POST["order_id"]
            order = Order.objects.filter(id=order_id)
            order.delete()

            orders = Order.objects.filter(name=request.user)

            return render(request, 'shop/checkout.html', context={'orders': orders} )

    else:
        orders = Order.objects.filter(name=request.user)




        return render(request, 'shop/checkout.html', context={'orders': orders})

# Оплата заказа class PayOrder()
def pay_orders(request, order_id):
    if request.method == 'POST':
        #
        pass
    # проверка оплаты -- смена статуса заказа -- перенаправление на страницу всех заказов

    else:
        return HttpResponseBadRequest('<h1>Форма---Оплата по карте---</h1><br>')

