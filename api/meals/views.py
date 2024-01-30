from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers


class UserMealListView(APIView):

    def get(self, request, *args, **kwargs):

        user_meals = models.UserMeal.objects.filter(
            user=request.user, 
            state__in=('none', 'liked')
        )

        serializer = serializers.UserMealSerializer(user_meals, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):

        user_meal_id = kwargs.get('pk')
        user_meal = models.UserMeal.objects.get(pk=user_meal_id)

        new_state = request.data.get('state')
        user_meal.state = new_state
        user_meal.save()

        serializer = serializers.UserMealSerializer(user_meal)
        return Response(serializer.data, status=status.HTTP_200_OK)