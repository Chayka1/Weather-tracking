import os

import requests
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from weather.models import Weather
from weather.serializers import WeatherSerializer

api_key = os.getenv("API_KEY", default="invalid")


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    @action(detail=False, methods=["post"])
    def get_weather(self, request, *args, **kwargs):
        # Десеріалізація запиту
        data = request.data
        city = data["city"]

        # Отримання інформації про погоду
        response_lat_lon = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}"
        )

        data = response_lat_lon.json()

        if data and len(data) > 0:
            weather = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?lat={data[0]["lat"]}&lon={data[0]["lon"]}&appid={api_key}'
            )

            data_weather = weather.json()

            temperature = data_weather["main"]["temp"] - 273.15
            temperature_feel = data_weather["main"]["feels_like"] - 273.15

            time = timezone.now()

            # Додавання запису в базу даних
            weather = Weather.objects.create(
                city=data[0]["name"],
                country=data[0]["country"],
                temperature=temperature,
                feels_like=temperature_feel,
                weather_description=data_weather["weather"][0]["description"],
                clouds=f"{data_weather['clouds']['all']}%",
                time=time,
            )

            # Серіалізація відповіді
            weather_data = WeatherSerializer(weather).data

            return Response(weather_data)

        else:
            return Response({"detail": "Город не найден!"}, status=400)

    @action(detail=False, methods=["get"])
    def search_history(self, request, *args, **kwargs):
        serializer = WeatherSerializer(self.queryset, many=True)
        return Response(serializer.data)
