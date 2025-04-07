#  Описание проекта "Effective_Mobile_Junior_Python" 

# .
django-admin startproject project .
pip install django
python manage.py startapp ads


python manage.py makemigrations
python manage.py migrate

python manage.py runserver
<a href="{% url 'board:advertisement_list' %}">Заявки на доставку</a>

python manage.py createsuperuser
