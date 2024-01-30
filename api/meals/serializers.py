from rest_framework import serializers

from . import models


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = ('name',)


class MealSerializers(serializers.ModelSerializer):

    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = models.Meal
        fields = ('name', 'instructions', 'ingredients')

    
class UserMealSerializer(serializers.ModelSerializer):

    meal = MealSerializers()

    class Meta:
        model = models.UserMeal
        fields = ('id', 'meal', 'state', 'timestamp')