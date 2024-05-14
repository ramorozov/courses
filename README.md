# courses
## Создание приложения

**Инициализация виртуальной среды courser/\.venv**

**Инсталяция пакета django ver. 4.0.8**\
#pipenv install django==4.0.8

**Активация виртуальной среды**\
#pipenv shell

**Инициализация проекта django**\
#django-admin startproject base .

**Запуск сервера django**\
#/courses/python manage.py runserver\
Чтобы указать конкреный порт\
#/courses/python manage.py runserver <номер_порта>\

**WSGI и ASGI**\
WSGI - интерфейс взаимодействия между web-сервером и приложением python\
ASGI - асинхронный интерфейс взаимодействия с серверами

**Создание приложения shop**\
#/courses/python manage.py startapp shop\

## Базы данных и миграции

**Применение миграции БД**
#python manage.py migrate