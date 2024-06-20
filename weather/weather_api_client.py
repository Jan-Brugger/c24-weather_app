from datetime import date, datetime
from typing import Any, Dict

import requests
from rest_framework.exceptions import APIException

from weather.models import ImportRequest


class WeatherApiClient:
    API_ENDPOINT = 'http://127.0.0.1:8000/weather-archive/temperature-range'

    def fetch_temperatures(self, request: ImportRequest) -> Dict[date, float]:
        request_params = self.__build_request_params(request)
        response = requests.get(self.API_ENDPOINT, request_params, timeout=10)

        if response.status_code != 200:
            raise APIException(
                f'Api-client returned a bad response. Status: {response.status_code}. Response: {response.text}'
            )

        parsed_response = self.__parse_response(response.json())

        return parsed_response

    @classmethod
    def __build_request_params(cls, request: ImportRequest):
        return {
            'latitude': request.latitude,
            'longitude': request.longitude,
            'from_date': date(year=request.year, month=1, day=1),
            'to_date': date(year=request.year, month=12, day=31),
            'filter_by_hour': request.hour_of_the_day
        }

    @classmethod
    def __parse_response(cls, response_body: dict[str, Any]) -> Dict[date, float]:
        temperatures = response_body.get('temperatures')

        if not temperatures or not isinstance(temperatures, dict):
            raise APIException('Api-client did not return any temperatures')

        return {datetime.fromisoformat(dt).date(): temp for dt, temp in temperatures.items()}
