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

**Применение миграции БД**\
#python manage.py migrate

**Создание суперюзера**\
#python manage.py createsuperuser

**Создание миграций для БД**\
Создает миграции за всех зарегестрированных в проекте приложений\
#python manage.py makemigrations

**Открытие в строенную оболочку**\
#python manage.py shell

**Заполнение БД Category через shell**\
#from shop.model import Category, Course\
Получение всех данных из БД Course\
#Course.objects.all()\
Получение всех данных из БД Category\
#Category.objects.all()\
Добавление данных в БД Category\
#new_category = Category(title='Programming')\
#Сохранение данных\
#new_category.save()

**Получение данных из БД через shell**\
#new_category.title\
#new_category.id\
#new_category.created_at

**Получение данных из БД через shell по primary key**\
#Category.objects.get(pk=1)\
#Category.objects.get(pk=1).id\
#Category.objects.get(pk=1).title\
#Category.objects.get(pk=1).created_at

**Фильтрация данных в БД через shell**\
#Category.objects.filter(pk=1)\
#Category.objects.filter(title='Programming')

**Добавление курсов в категорию в БД через shell**\
Получение данных из БД Category по id\
#category = Category.objects.get(id=1)\
Получение всех данных из БД Category\
#category.course_set.all()\
Добавление курса в БД\
#category.course_set.create(title='Python', price=99.99, students_qty=100, reviews_qty=20)

**Получение списка курсов из БД через shell**\
#[course.title for course in Course.objects.all()]