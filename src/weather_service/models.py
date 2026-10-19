"""Data models used by the weather service."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ForecastRequest:
    """A request for the weather forecast of a city.

    Attributes:
        city: Name of the city to get the forecast for.
        api_key: Key used to authenticate with the weather provider.
            Hidden from ``repr`` so it never leaks into logs.
    """

    city: str
    api_key: str = field(repr=False)


@dataclass(frozen=True)
class Forecast:
    """The weather forecast for a city.

    Attributes:
        city: Name of the city the forecast is for.
        temperature_c: Temperature in degrees Celsius.
        condition: Short description of the weather, e.g. "Sunny".
        humidity: Relative humidity as a percentage (0-100).
    """

    city: str
    temperature_c: float
    condition: str
    humidity: int