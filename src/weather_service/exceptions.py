"""Custom exceptions raised by the weather service."""


class WeatherServiceError(Exception):
    """Base class for all errors raised by the weather service."""


class InvalidAPIKeyError(WeatherServiceError):
    """Raised when the API key is missing or not valid."""

    def __init__(self) -> None:
        """Create the error with a standard message."""
        super().__init__("Invalid API key")


class CityNotFoundError(WeatherServiceError):
    """Raised when no forecast exists for the requested city.

    Attributes:
        city: The city that could not be found.
    """

    def __init__(self, city: str) -> None:
        """Create the error for the given city.

        Args:
            city: The city that could not be found.
        """
        super().__init__(f"City not found: {city}")
        self.city = city