from rest_framework import serializers
from .models import Weather


class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('airTemperature', 'pressure', 'windDirection', 'windSpeed',
                  'visibility', 'waterTemperature', 'cloudCover')
