from django.urls import path

from weather.views import DeleteWeatherList, ImportWeatherList, WeatherList

urlpatterns = [
    path('', WeatherList.as_view()),
    path('delete/', DeleteWeatherList.as_view()),
    path('import/', ImportWeatherList.as_view())
]
