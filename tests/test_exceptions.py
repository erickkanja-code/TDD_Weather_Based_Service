"""Tests for the custom weather service exceptions."""

from weather_service.exceptions import (
    CityNotFoundError,
    InvalidAPIKeyError,
    WeatherServiceError,
)


def test_weather_service_error_is_an_exception():
    assert issubclass(WeatherServiceError, Exception)


def test_invalid_api_key_error_is_a_weather_service_error():
    assert issubclass(InvalidAPIKeyError, WeatherServiceError)


def test_city_not_found_error_is_a_weather_service_error():
    assert issubclass(CityNotFoundError, WeatherServiceError)


def test_invalid_api_key_error_has_clear_message():
    error = InvalidAPIKeyError()

    assert str(error) == "Invalid API key"


def test_city_not_found_error_includes_city():
    error = CityNotFoundError("Atlantis")

    assert error.city == "Atlantis"
    assert str(error) == "City not found: Atlantis"