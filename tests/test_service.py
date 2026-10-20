"""Tests for the WeatherService."""

import pytest

from weather_service.exceptions import CityNotFoundError, InvalidAPIKeyError
from weather_service.mock_provider import VALID_API_KEY, MockWeatherProvider
from weather_service.models import Forecast, ForecastRequest
from weather_service.provider import WeatherProvider
from weather_service.service import WeatherService

LONDON_FORECAST = Forecast("London", 15.0, "Cloudy", 80)


@pytest.fixture
def mock_provider(mocker):
    return mocker.Mock(spec=WeatherProvider)


@pytest.fixture
def service(mock_provider):
    return WeatherService(provider=mock_provider, api_key="test-key")


def test_get_forecast_returns_forecast_from_provider(service, mock_provider):
    mock_provider.fetch_forecast.return_value = LONDON_FORECAST

    forecast = service.get_forecast("London")

    assert forecast == LONDON_FORECAST


def test_get_forecast_sends_city_and_api_key_to_provider(service, mock_provider):
    service.get_forecast("London")

    mock_provider.fetch_forecast.assert_called_once_with(
        ForecastRequest(city="London", api_key="test-key")
    )


@pytest.mark.parametrize("error", [InvalidAPIKeyError(), CityNotFoundError("Atlantis")])
def test_get_forecast_passes_provider_errors_to_caller(service, mock_provider, error):
    mock_provider.fetch_forecast.side_effect = error

    with pytest.raises(type(error)):
        service.get_forecast("London")


def test_service_works_with_real_mock_provider():
    service = WeatherService(provider=MockWeatherProvider(), api_key=VALID_API_KEY)

    assert service.get_forecast("London") == LONDON_FORECAST