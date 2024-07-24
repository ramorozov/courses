"""
Файл маршрутизации приложения Mainpage
"""

from django.urls import path
from . import views

#Роутинг с учетом приложений
app_name = 'mainpage'

#Маршрут на главную сраницу '' 
#приложения Shop views.index 
#с названием 'index'
urlpatterns = [
    path('', views.index, name='index')
]