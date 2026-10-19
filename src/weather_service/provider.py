"""The interface that every weather provider must follow."""

from abc import ABC, abstractmethod

from weather_service.models import Forecast, ForecastRequest


class WeatherProvider(ABC):
    """A source of weather forecasts.

    The weather service depends only on this interface, so a mock provider
    can be swapped for a real API provider without changing the service.
    """

    @abstractmethod
    def fetch_forecast(self, request: ForecastRequest) -> Forecast:
        """Fetch the weather forecast for the requested city.

        Args:
            request: The city to look up and the API key to authenticate with.

        Returns:
            The forecast for the requested city.

        Raises:
            InvalidAPIKeyError: If the API key is not valid.
            CityNotFoundError: If there is no forecast for the city.
        """