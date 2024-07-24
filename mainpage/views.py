from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.
"""
Функция index отвечает за то, что будет возвращаться
при обращении на главную страницу приложения Mainpage
"""
def index(request):
    #return HttpResponse("Hello from the mainpage app")
    return render(request, 'mainpage/mainpage.html')