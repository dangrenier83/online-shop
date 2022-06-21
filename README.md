# online-shop

Online shop from the Django3 By Examples from Packt Publishings

To run:

1) Enter a python venv
2) pip install -r requirements.txt 
2) Run rabbitmq-server as root
3) Run celery celery -A myshop worker -l INFO
4) Run redis-server
5) python3 manage.py runserver