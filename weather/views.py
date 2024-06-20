from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from weather.models import ImportRequest, WeatherRecord
from weather.serializers import ImportRequestSerializer, WeatherRecordSerializer
from weather.weather_api_client import WeatherApiClient


class WeatherList(ListCreateAPIView):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherRecordSerializer

    @classmethod
    def delete(cls, *args, **kwargs):
        WeatherRecord.objects.all().delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ImportWeatherList(GenericAPIView):
    serializer_class = ImportRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = ImportRequestSerializer(data=request.data)
        if serializer.is_valid():
            self.__import_data(ImportRequest(**serializer.validated_data))

            return Response('data imported', status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def __import_data(cls, request: ImportRequest) -> None:
        new_records = WeatherApiClient().fetch_temperatures(request)

        WeatherRecord.objects.all().delete()

        for date, temp in new_records.items():
            WeatherRecord(date=date, temperature=temp).save()
