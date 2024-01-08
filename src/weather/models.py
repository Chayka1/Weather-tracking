from datetime import datetime

from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    temperature = models.FloatField()
    feels_like = models.FloatField()
    weather_description = models.CharField(max_length=255)
    clouds = models.CharField(max_length=4)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.city}, {self.country}:{self.temperature}, {self.time}"
