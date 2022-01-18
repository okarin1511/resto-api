
from rest_framework import serializers
from .models import Restaurant, Timings


class TimingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timings
        fields = [
            'id',
            'opening_time_mon',
            'closing_time_mon',
            'opening_time_tue',
            'closing_time_tue',
            'opening_time_wed',
            'closing_time_wed',
            'opening_time_thu',
            'closing_time_thu',
            'opening_time_fri',
            'closing_time_fri',
            'opening_time_sat',
            'closing_time_sat',
            'opening_time_sun',
            'closing_time_sun'
        ]

class RestaurantSerializer(serializers.ModelSerializer):
    timings = TimingsSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'type',
            'desc',
            'timings'
        ]

