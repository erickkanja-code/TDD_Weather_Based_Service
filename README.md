# Weather Service

A mock weather API service built with strict Test-Driven Development (TDD).
It does not call a real API. It simulates one, returning predefined forecasts
for known cities and raising specific errors for invalid input.

## Features

- `WeatherService.get_forecast(city)` returns a forecast for a known city.
- Custom errors: `InvalidAPIKeyError` and `CityNotFoundError`, both subclasses
  of `WeatherServiceError`.
- Structured `key=value` logging of every request, response and error.
- The service depends on the abstract `WeatherProvider` interface, so the mock
  provider can be swapped for a real API provider without changing the service.

Known cities: London, Paris, Tokyo, New York (case-insensitive).

## Project structure

```
src/weather_service/
    models.py          ForecastRequest and Forecast dataclasses
    exceptions.py      Custom exceptions
    provider.py        Abstract WeatherProvider interface
    mock_provider.py   MockWeatherProvider with predefined data
    service.py         WeatherService with logging
tests/                 pytest test suite
```

## Setup

Requires Python and [Poetry](https://python-poetry.org/).

```bash
poetry install
poetry run pre-commit install
```

## Usage

```python
import logging

from weather_service.exceptions import CityNotFoundError
from weather_service.mock_provider import VALID_API_KEY, MockWeatherProvider
from weather_service.service import WeatherService

logging.basicConfig(level=logging.INFO)

service = WeatherService(provider=MockWeatherProvider(), api_key=VALID_API_KEY)
print(service.get_forecast("London"))

try:
    service.get_forecast("Atlantis")
except CityNotFoundError as error:
    print(error)
```

## Running tests

```bash
poetry run pytest --cov
```

Coverage is measured by `coverage.py` (through `pytest-cov`), and the run fails
if coverage drops below 100%.

## Code quality

Black (formatting) and ruff (linting, Google-style docstrings, type hints) run
automatically before every commit through pre-commit. To run them manually:

```bash
poetry run pre-commit run --all-files
```

## Development workflow

- **TDD:** every feature starts with a failing test commit (`test: ...`),
  followed by the code that makes it pass (`feat: ...`).
- **Trunk-based development:** `main` is always working. Each change is made on
  a short-lived branch and merged through a reviewed pull request.
