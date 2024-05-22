from django.contrib import admin
from . import models

#Регистрация моделей Course и Category
admin.site.register(models.Category)
admin.site.register(models.Course)