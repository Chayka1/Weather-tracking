from django.urls import include, path
from rest_framework.routers import DefaultRouter

from weather.api import WeatherViewSet

router = DefaultRouter()
router.register("", WeatherViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
