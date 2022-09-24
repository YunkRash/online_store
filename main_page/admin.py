from django.contrib import admin
from . import models

# Register your models here.
# Добавляем админ панель и создаем пользователя
admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.UserCart)
