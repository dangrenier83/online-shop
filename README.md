# online-shop

Online shop from the Django3 By Examples from Packt Publishings

To run:

1. Enter a python venv
1. Install the required libraries using this pip command: 
`pip install -r requirements.txt`
1. Start the rabbitmq-server broker as root
1. Start the celery worker with the following command :
`celery -A myshop worker -l INFO`
1. Start Redis with : 
`redis-server`
1. Start the Django Application with:
`python3 manage.py runserver`