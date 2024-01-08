from rest_framework import serializers

from weather.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    temperature = serializers.IntegerField()
    feels_like = serializers.IntegerField()
    time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Weather
        fields = [
            "id",
            "city",
            "country",
            "temperature",
            "feels_like",
            "weather_description",
            "clouds",
            "time",
        ]
