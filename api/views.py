from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from datetime import datetime as date

from .serializers import RestaurantSerializer
from .models import Restaurant, Timings

# Create your views here.
class RestaurantStatus(APIView):

    def get_object(self, type):
        try:
            return Restaurant.objects.filter(type=type).all()

        except Restaurant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, type):

        day = date.today().strftime("%A")

        restaurant = Restaurant.objects.filter(type=type).all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data)
