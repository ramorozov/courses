from django.contrib import admin
from . import models

#Изменение заголовков панели администрирования
admin.site.site_header = "Courses admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Wellcome to the Courses admin area"

#Отображаем дополнительные поля курсов в панели администрирования
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')

#Отображаем дополнительные поля категорий в панели администрирования
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

#Регистрация моделей Course и Category
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)