"""Basic configuration."""

from frozendict import frozendict

APP_START_URL = 'http://et2test.4th-dimension.cz/admin/'
BROWSER_SETTINGS = frozendict({
    'ignoreHTTPSErrors': True,
    'headless': False,  # todo use env
    'defaultViewport': {
        'width': 1920,
        'height': 1200,
    },
    'args': ['--start-maximized'],
})
SEARCH_ELEMENT_TIMEOUT = 5000
