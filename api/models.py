from tastypie.resources import ModelResource
from shop.models import Category, Course

# Create your models here.
class CategoryResource(ModelResource):
    class Meta:
        #Получение всех категорий курсов
        queryset = Category.objects.all()
        resource_name = 'categories'
        #Разрешене только на чтение, метод get
        allowed_mathods = ['get']

class CourseResource(ModelResource):
    class Meta:
        #Получение всех курсов
        queryset = Course.objects.all()
        resource_name = 'courses'
        #Разрешене только на чтение, запись, удаление (метод get, post, delete)
        allowed_mathods = ['get', 'post', 'delete']
