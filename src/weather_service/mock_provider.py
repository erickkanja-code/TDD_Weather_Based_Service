"""A mock weather provider that simulates a real weather API."""

from weather_service.exceptions import CityNotFoundError, InvalidAPIKeyError
from weather_service.models import Forecast, ForecastRequest
from weather_service.provider import WeatherProvider

VALID_API_KEY = "mock-api-key"

KNOWN_FORECASTS: dict[str, Forecast] = {
    "london": Forecast(
        city="London", temperature_c=15.0, condition="Cloudy", humidity=80
    ),
    "paris": Forecast(city="Paris", temperature_c=18.0, condition="Sunny", humidity=60),
    "tokyo": Forecast(city="Tokyo", temperature_c=22.0, condition="Rainy", humidity=75),
    "new york": Forecast(
        city="New York", temperature_c=20.0, condition="Windy", humidity=65
    ),
}


class MockWeatherProvider(WeatherProvider):
    """A fake weather API that returns predefined forecasts.

    Only ``VALID_API_KEY`` is accepted, and only the cities in
    ``KNOWN_FORECASTS`` can be found. City names are case-insensitive.
    """

    def fetch_forecast(self, request: ForecastRequest) -> Forecast:
        """Return the predefined forecast for the requested city.

        Args:
            request: The city to look up and the API key to authenticate with.

        Returns:
            The predefined forecast for the city.

        Raises:
            InvalidAPIKeyError: If the API key is not ``VALID_API_KEY``.
            CityNotFoundError: If the city is not in ``KNOWN_FORECASTS``.
        """
        if request.api_key != VALID_API_KEY:
            raise InvalidAPIKeyError()

        forecast = KNOWN_FORECASTS.get(request.city.lower())
        if forecast is None:
            raise CityNotFoundError(request.city)

        return forecast