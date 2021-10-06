"""Basic configuration."""

from frozendict import frozendict

APP_START_URL = 'http://et2test.4th-dimension.cz/admin/'
BROWSER_SETTINGS = frozendict({
    'ignoreHTTPSErrors': True,
    'headless': False,  # todo use env
    'defaultViewport': {
        'width': 1980,
        'height': 1060,
    },
    'args': ['--start-maximized'],
})
SEARCH_ELEMENT_TIMEOUT = 5000
