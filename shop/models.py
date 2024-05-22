from django.db import models

from django.utils import timezone

#Создание модели для категорий курсов
class Category(models.Model):
    #Задаем поля БД и их параметры
    #Заголовок категории, символы, 255 символов
    title = models.CharField(max_length=255)
    #Время создания категории, дата, текущая дата генерируется автоматически
    created_at = models.DateTimeField(default=timezone.now)
    #Отображение заголовков категорий в admin-панели
    def __str__(self):
        return self.title


#Создание модели для курсов

class Course(models.Model):
    title = models.CharField(max_length=255)
    #Цена число с плавающей точкой
    price = models.FloatField()
    #Кол-во студентов, целое число
    students_qty = models.IntegerField()
    #Количество отзывов
    reviews_qty = models.IntegerField()
    #Категории связаны с моделью Category, 
    #будут удалятся все курсы при удалении категории
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    #Отображение заголовков категорий в admin-панели
    def __str__(self):
        return self.title