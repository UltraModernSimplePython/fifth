import click
import requests

# API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language="en"):  # this is not a guaranteed keyword argument
    try:
        with requests.get(API_URL.format(language=language), timeout=10) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message) from error
