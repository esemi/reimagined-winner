"""Basic configuration."""

from frozendict import frozendict

APP_HOSTNAME = 'http://et2test.4th-dimension.cz'
APP_START_URL = f'{APP_HOSTNAME}/admin/'
CLEAR_DB_URL = f'{APP_HOSTNAME}/purge-test-db'

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
