from rest_framework import serializers

from weather.models import ImportRequest, WeatherRecord


class WeatherRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherRecord
        fields = ['date', 'temperature']
        ordering = ['date']


class ImportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportRequest
        fields = ['latitude', 'longitude', 'year', 'hour_of_the_day']
