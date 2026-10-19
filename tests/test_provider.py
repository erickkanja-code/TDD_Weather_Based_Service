"""Tests for the WeatherProvider interface."""

import pytest

from weather_service.models import Forecast, ForecastRequest
from weather_service.provider import WeatherProvider


def test_weather_provider_cannot_be_instantiated():
    with pytest.raises(TypeError):
        WeatherProvider()


def test_provider_without_fetch_forecast_cannot_be_instantiated():
    class IncompleteProvider(WeatherProvider):
        pass

    with pytest.raises(TypeError):
        IncompleteProvider()


def test_provider_with_fetch_forecast_can_be_used():
    class FakeProvider(WeatherProvider):
        def fetch_forecast(self, request):
            return Forecast(
                city=request.city, temperature_c=20.0, condition="Sunny", humidity=50
            )

    provider = FakeProvider()
    forecast = provider.fetch_forecast(ForecastRequest(city="Paris", api_key="key"))

    assert forecast.city == "Paris"