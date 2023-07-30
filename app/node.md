python manage.py runserver
long123
tranvanchilong@gmail.com
a0977293389
python manage.py makemigrations
python manage.py migrate 
python manage.py createsuperuser

docker run --name docker_django_ecommerce -p 5003:8000 -it -v ${PWD}/app:/app:rw api_django /bin/bash


pip install django-cors-headers
pip install -U djoser
pip install Pillow
pip install stripe-django