#  Описание проекта "Effective_Mobile_Junior_Python" 

# .
django-admin startproject project .
pip install django
python manage.py startapp ads


python manage.py makemigrations --merge
python manage.py migrate

python manage.py runserver


python manage.py createsuperuser

# Запуск всех тестов
python manage.py test

# Запуск тестов конкретного приложения
python manage.py test myapp

# Запуск конкретного тестового класса
python manage.py test myapp.tests.AnimalTestCase

# Запуск конкретного тестового метода
python manage.py test myapp.tests.AnimalTestCase.test_animals_can_speak

# Сохранение тестовой базы данных 
python manage.py test --keepdb

# Параллельное выполнение тестов
python manage.py test --parallel
