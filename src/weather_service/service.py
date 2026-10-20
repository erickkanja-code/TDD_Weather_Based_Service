"""The weather service that clients use to get forecasts."""

import logging

from weather_service.exceptions import WeatherServiceError
from weather_service.models import Forecast, ForecastRequest
from weather_service.provider import WeatherProvider

logger = logging.getLogger(__name__)


class WeatherService:
    """Gets weather forecasts from a weather provider.

    The service depends only on the abstract ``WeatherProvider`` interface,
    so any provider, mock or real, can be passed in.
    """

    def __init__(self, provider: WeatherProvider, api_key: str) -> None:
        """Create the service.

        Args:
            provider: The source of weather data.
            api_key: The key sent to the provider with every request.
        """
        self._provider = provider
        self._api_key = api_key

    def get_forecast(self, city: str) -> Forecast:
        """Get the weather forecast for a city.

        Every request, response and error is logged.

        Args:
            city: Name of the city to get the forecast for.

        Returns:
            The forecast for the city.

        Raises:
            InvalidAPIKeyError: If the provider rejects the API key.
            CityNotFoundError: If the provider has no forecast for the city.
        """
        logger.info("event=forecast_requested city=%s", city)
        request = ForecastRequest(city=city, api_key=self._api_key)

        try:
            forecast = self._provider.fetch_forecast(request)
        except WeatherServiceError as error:
            logger.warning("event=forecast_failed city=%s error=%s", city, error)
            raise

        logger.info(
            "event=forecast_returned city=%s temperature_c=%s condition=%s",
            forecast.city,
            forecast.temperature_c,
            forecast.condition,
        )
        return forecast