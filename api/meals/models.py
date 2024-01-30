from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Meal(models.Model):

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name='meals')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class UserMeal(models.Model):

    STATE_CHOICES = (
        ('none', 'None'),
        ('liked', 'Liked'),
        ('disliked', 'Disliked'),
        ('ignored', 'Ignored'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=10,
        choices=STATE_CHOICES,
        default='none',
        help_text='vote your meals'
    )
    timestamp = models.DateTimeField(auto_now_add=True)