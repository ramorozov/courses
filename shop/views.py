from django.shortcuts import render
from django.http import HttpResponse
#Импортируем модель Course
from .models import Course

# Create your views here.
"""
Функция index отвечает за то, что будет возвращаться
при обращении на главную страницу приложения Shop
"""
def index(request):
    #Получение списка курсов
    courses = Course.objects.all()
    #Формируем список курсов, делаем перенос и объединяем в одну строку
    #return HttpResponse(''.join([str(course) + '<br>' for course in courses]))

    #Вывод страницы шаблона
    #return render(request, 'courses.html')

    #Вывод данных в шаблон courses
    return render(request, 'courses.html', {'courses': courses})

"""
Функция single_course отвечает за то, что будет возвращаться
при обращении на страницу курса приложения Shop
"""
def single_course(request, course_id):
    #Поиск курса по primary key
    course = Course.objects.get(pk=course_id)
    #Рендеринг шаблона single_course.html
    return render(request, 'single_course.html', {'course': course})