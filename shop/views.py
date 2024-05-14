from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
Функция index отвечает за то, что будет возващаться
при обращении на главную страницу приложения Shop
"""
def index(request):
    return HttpResponse("Hello from the Shop app")
