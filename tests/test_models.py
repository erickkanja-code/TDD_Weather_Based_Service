"""Tests for the weather data models."""

import dataclasses

import pytest

from weather_service.models import Forecast, ForecastRequest


def test_forecast_request_stores_city_and_api_key():
    request = ForecastRequest(city="London", api_key="secret-key")

    assert request.city == "London"
    assert request.api_key == "secret-key"


def test_forecast_request_hides_api_key_in_repr():
    request = ForecastRequest(city="London", api_key="secret-key")

    assert "secret-key" not in repr(request)


def test_forecast_stores_weather_data():
    forecast = Forecast(
        city="London", temperature_c=15.0, condition="Cloudy", humidity=80
    )

    assert forecast.city == "London"
    assert forecast.temperature_c == 15.0
    assert forecast.condition == "Cloudy"
    assert forecast.humidity == 80


def test_forecast_is_immutable():
    forecast = Forecast(
        city="London", temperature_c=15.0, condition="Cloudy", humidity=80
    )

    with pytest.raises(dataclasses.FrozenInstanceError):
        forecast.temperature_c = 30.0