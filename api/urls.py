from django.urls import path 
from .views import RestaurantStatus

urlpatterns = [
    path('restaurants/<str:type>/', RestaurantStatus.as_view())
]

