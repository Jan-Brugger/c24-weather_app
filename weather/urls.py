from django.urls import path

from weather.views import ImportWeatherList, WeatherList

urlpatterns = [
    path('', WeatherList.as_view()),
    path('import/', ImportWeatherList.as_view())
]
