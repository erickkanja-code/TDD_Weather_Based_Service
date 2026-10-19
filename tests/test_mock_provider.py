"""Tests for the MockWeatherProvider."""

import pytest

from weather_service.exceptions import CityNotFoundError, InvalidAPIKeyError
from weather_service.mock_provider import VALID_API_KEY, MockWeatherProvider
from weather_service.models import Forecast, ForecastRequest
from weather_service.provider import WeatherProvider


def test_mock_provider_is_a_weather_provider():
    assert isinstance(MockWeatherProvider(), WeatherProvider)


@pytest.mark.parametrize(
    ("city", "expected"),
    [
        ("London", Forecast("London", 15.0, "Cloudy", 80)),
        ("Paris", Forecast("Paris", 18.0, "Sunny", 60)),
        ("Tokyo", Forecast("Tokyo", 22.0, "Rainy", 75)),
        ("New York", Forecast("New York", 20.0, "Windy", 65)),
    ],
)
def test_returns_forecast_for_known_city(city, expected):
    provider = MockWeatherProvider()
    request = ForecastRequest(city=city, api_key=VALID_API_KEY)

    assert provider.fetch_forecast(request) == expected


@pytest.mark.parametrize("city", ["london", "LONDON", "lOnDoN"])
def test_city_lookup_ignores_case(city):
    provider = MockWeatherProvider()
    request = ForecastRequest(city=city, api_key=VALID_API_KEY)

    assert provider.fetch_forecast(request).city == "London"


@pytest.mark.parametrize("api_key", ["wrong-key", ""])
def test_raises_invalid_api_key_error_for_bad_key(api_key):
    provider = MockWeatherProvider()
    request = ForecastRequest(city="London", api_key=api_key)

    with pytest.raises(InvalidAPIKeyError):
        provider.fetch_forecast(request)


@pytest.mark.parametrize("city", ["Atlantis", "Londonn", ""])
def test_raises_city_not_found_error_for_unknown_city(city):
    provider = MockWeatherProvider()
    request = ForecastRequest(city=city, api_key=VALID_API_KEY)

    with pytest.raises(CityNotFoundError) as exc_info:
        provider.fetch_forecast(request)

    assert exc_info.value.city == city


def test_checks_api_key_before_city():
    provider = MockWeatherProvider()
    request = ForecastRequest(city="Atlantis", api_key="wrong-key")

    with pytest.raises(InvalidAPIKeyError):
        provider.fetch_forecast(request)