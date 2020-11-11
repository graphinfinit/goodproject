


'''





import uuid
from yandex_checkout import Configuration, Payment







Configuration.account_id = '<Идентификатор магазина>' # в тестовом варианте начинается с test_
Configuration.secret_key = '<Секретный ключ>'






payment = Payment.create({
    "amount": {
        "value": "10.00",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://www.merchant-website.com/return_url"
    },
    "capture": True,
    "description": "Заказ №1"

















from yandex_checkout import Payment
import uuid

idempotence_key = str(uuid.uuid4())
payment = Payment.create({
    "amount": {
      "value": "2.00",
      "currency": "RUB"
    },
    "payment_method_data": {
      "type": "bank_card"
    },
    "confirmation": {
      "type": "redirect",
      "return_url": "https://www.merchant-website.com/return_url"
    },
    "description": "Заказ №72"}, idempotence_key)

# get confirmation url
confirmation_url = payment.confirmation.confirmation_url


'''









'''

Примеры
https://github.com/yoomoney/yandex-checkout-sdk-python


ЯндексКАсса объект Оплата
{
  "id": "22e12f66-000f-5000-8000-18db351245c7",
  "status": "waiting_for_capture",
  "paid": true,
  "amount": {
    "value": "2.00",
    "currency": "RUB"
  },
  "created_at": "2018-07-18T10:51:18.139Z",
  "description": "Заказ №72",
  "expires_at": "2018-07-25T10:52:00.233Z",
  "metadata": {},
  "payment_method": {
    "type": "bank_card",
    "id": "22e12f66-000f-5000-8000-18db351245c7",
    "saved": false,
    "card": {
      "first6": "555555",
      "last4": "4444",
      "expiry_month": "07",
      "expiry_year": "2022",
      "card_type": "MasterCard",
      "issuer_country": "RU",
      "issuer_name": "Sberbank"
    },
    "title": "Bank card *4444"
  },
  "recipient": {
    "account_id": "100001",
    "gateway_id": "1000001"
  },
  "refundable": false,
  "test": false
"income_amount": {
        "value": "1.97",
        "currency": "RUB"
    }
  }
  
  
  
  
  тело ответа
  
  
{
  "id": "22e12f66-000f-5000-8000-18db351245c7",
  "status": "pending",
  "paid": false,
  "amount": {
    "value": "2.00",
    "currency": "RUB"
  },
  "confirmation": {
    "type": "redirect",
    "return_url": "https://www.merchant-website.com/return_url",
    "confirmation_url": "https://money.yandex.ru/payments/external/confirmation?orderId=22e12f66-000f-5000-8000-18db351245c7"
  },
  "created_at": "2018-07-18T10:51:18.139Z",
  "description": "Заказ №72",
  "metadata": {
    
  },
  "payment_method": {
    "type": "bank_card",
    "id": "22e12f66-000f-5000-8000-18db351245c7",
    "saved": false
  },
  "recipient": {
    "account_id": "100001",
    "gateway_id": "1000001"
  },
  "refundable": false,
  "test": false
}
'''