"""
Файл маршрутизации приложения Shop
"""

from django.urls import path
from . import views

#Маршрут на главную сраницу '' 
#приложения Shop views.index 
#с названием 'index'
urlpatterns = [
    path('', views.index, name='index')
]