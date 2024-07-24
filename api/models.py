from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication

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
        #Исключение полей из ответа api
        excludes = ['reviews_qty','students_qty']
        #Добавляем аутентификацию и авторизацию
        authentication = CustomAuthentication()
        authorization = Authorization()


    '''Вставка категории курса в запросе'''
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle
    
    '''Получение категории курса в запросе'''
    def dehydrate(self, bundle):
        bundle.data['category'] = bundle.obj.category
        return bundle

