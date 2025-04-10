#  Описание проекта "Effective_Mobile_Junior_Python" 

# Создание проекта
django-admin startproject project .
pip install django
python manage.py startapp ads

# Установка виртуального окружения
pip install -r requirements.txt
pip freeze > requirements.txt

# Создание миграций
python manage.py makemigrations --merge
python manage.py migrate

# Запуск приложения 
python manage.py runserver

# Создание учетной записи администратора
python manage.py createsuperuser
Username (leave blank to use 'tsars'): tsars
Email address: test@example.com
Password: 123456789


# Запуск всех тестов
python manage.py test



![Uploading 1.png…](https://github.com/SergeyTsVL/TZ_vacancy/blob/main/images/1.png)


