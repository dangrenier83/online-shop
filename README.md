# online-shop

Online shop from the Django3 By Examples from Packt Publishings

To run:

1) Run rabbitmq-server as root
2) Run celery celery -A myshop worker -l INFO
3) Run redis-server
4) python3 manage.py runserver