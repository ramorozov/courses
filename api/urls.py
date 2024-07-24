from django.urls import path, include
from api.models import CourseResource, CategoryResource
from tastypie.api import Api

#Создаем экземпляр класса Api
api = Api(api_name = 'v1')
#Создадим экземляры класса CourseResource, CategoryResource
course_resource = CourseResource()
category_resource = CategoryResource()
#Регестрируем course_resource, category_resource в api
api.register(course_resource)
api.register(category_resource)

urlpatterns = [
    #Маршрутизация приложения Api
    path('', include(api.urls), name='index')
]