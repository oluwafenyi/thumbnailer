# thumbnailer
An image resizing webapp built with Django and a sprinkle of Vue.js. Built in the process of learning about celery with Adam McQuistan's article: https://stackabuse.com/asynchronous-tasks-in-django-with-redis-and-celery/

### Required:
- Python3
- Redis

### Steps:
- Clone Repository
- Create and initialize Python3 Virtual Enviroment
- Install requirements
- Launch redis server in one terminal tab: `redis-server`
- Run celery worker in another tab within the virtual environment: `celery worker -A image_parroter --loglevel=info`
- Start Django Server in another tab: `python manage.py runserver`
