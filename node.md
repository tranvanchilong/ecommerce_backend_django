# chạy project 

docker-compose -f docker-compose-test.yml up

# host


python -m django startproject ecommerce
python .\manage.py startapp product

docker run --name docker_django_ecommerce_login -p 5004:8000 -it -v ${PWD}/app:/app:rw api_django /bin/bash

python manage.py runserver 0.0.0.0:8000

pip install django-cors-headers
pip install -U djoser
pip install Pillow
pip install stripe-django


python manage.py runserver
long123
tranvanchilong@gmail.com
a0977293389
python manage.py makemigrations
python manage.py migrate 
python manage.py createsuperuser


'corsheaders.middleware.CorsMiddleware',
