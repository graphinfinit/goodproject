# djangoherbs


Для тестировки

0) python manage.py makemigrations; python manage.py migrate; python manage.py createsuperuser;

1)Запустить на localhost django: python manage.py runserver;

2)запустить Celery : celery -A django_herbs worker -l INFO;

3)запустить key-value базу Redis redis :тест на win64 https://github.com/microsoftarchive/redis/releases/tag/win-3.2.100 и запустить exe файл; 
redis linux :https://redis.io/download (если использовать RabbitMQ : запустить rabbitmq-server)

4)smtp-сервер для разработки: python -m smtpd -n -c DebuggingServer 127.0.0.1:25 (на данный момент используется smtp сервер gmail: user = ***@gmail.com)

5)заполнить тестовые данные через admin-ку и формы.Например статусы заказа.
