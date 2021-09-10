"""Basic configuration."""

from frozendict import frozendict

APP_START_URL = 'https://dsbot.ru/'  # todo use Path
BROWSER_SETTINGS = frozendict({
    'ignoreHTTPSErrors': True,
    # todo use env
    'headless': False,
    'defaultViewport': {
        'width': 1980,
        'height': 1060,
    },
    'args': ['--start-maximized'],
})
SEARCH_ELEMENT_TIMEOUT = 5000
