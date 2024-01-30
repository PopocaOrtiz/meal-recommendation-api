from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import requests

from api.meals import models


MEALS_BASEPATH_API = "https://www.themealdb.com/api/json/v1/1/"


def get_assign_method():
    import random
    return random.choice(['random', 'ingredient', 'category', 'area'])


def save_meal_and_ingredients(meal_data):

    meal, created = models.Meal.objects.get_or_create(
        name=meal_data['strMeal'],
        instructions=meal_data['strInstructions']
    )

    ingredients = []
    for i in range(1, 20):
        ingredient_name = meal_data.get(f'strIngredient{i}')
        if ingredient_name:
            ingredient, created = models.Ingredient.objects.get_or_create(name=ingredient_name)
            ingredients.append(ingredient)

    meal.ingredients.set(ingredients)

    return meal


def assign_meal(meal, user):

    user_meal, created = models.UserMeal.objects.get_or_create(
        user=user,
        meal=meal,
    )

    return user_meal


def assign_new_meals():

    for user in User.objects.all():

        method = get_assign_method()
        url = MEALS_BASEPATH_API

        match method:
            case 'random':
                url += "random.php"
            case 'ingredient':
                random_ingredient = models.Ingredient.objects.order_by('?').first()
                url += f"filter.php?i={random_ingredient.name}" if random_ingredient else "random.php"
            case 'category':
                random_meal = models.Meal.objects.order_by('?').first()
                url += f"filter.php?c={random_meal.category}" if random_meal else "random.php"
            case 'area':
                random_meal = models.Meal.objects.order_by('?').first()
                url += f"filter.php?c={random_meal.area}" if random_meal else "random.php"

        response = requests.get(url)

        if response.status_code != 200:
            continue

        meals = response.json()['meals']

        if not meals:
            continue

        meal = save_meal_and_ingredients(meals[0])
        assign_meal(meal, user)
        

class Command(BaseCommand):

    help = "assign a new meal to every user"
            
    def handle(self, *args, **kwargs):

        assign_new_meals()

        self.stdout.write(self.style.SUCCESS('Successfully executeed assign new meals'))