from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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
    return render(request, 'shop/courses.html', {'courses': courses})

"""
Функция single_course отвечает за то, что будет возвращаться
при обращении на страницу курса приложения Shop
"""
def single_course(request, course_id):
    try:
        #Поиск курса по primary key
        course = Course.objects.get(pk=course_id)
        #Рендеринг шаблона single_course.html
        return render(request, 'shop/single_course.html', {'course': course})
    #Ошибка 404 если урс не найден
    except Course.DoesNotExist:
        raise Http404()
    #Ошибка 404, способ - 2
    #course = get_object_or_404(Courses, pk=course_id)
    #return render(request, 'single_course.html', {'course': course})