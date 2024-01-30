from django.contrib import admin

from . import models


admin.site.register(models.Ingredient)
admin.site.register(models.Meal)
admin.site.register(models.UserMeal)
