from django.shortcuts import render
from django.http import HttpResponse
#Импортируем модель Course
from .models import Course

# Create your views here.
"""
Функция index отвечает за то, что будет возващаться
при обращении на главную страницу приложения Shop
"""
def index(request):
    #Получение списка курсов
    courses = Course.objects.all()
    #Формируем список курсов, делаем перенос и объединяем в одну строку
    #return HttpResponse(''.join([str(course) + '<br>' for course in courses]))

    #Вывод страницы шаблона
    return render(request, 'courses.html')
