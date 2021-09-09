# todo use Path
APP_START_URL = 'https://dsbot.ru/'
BROWSER_SETTINGS = {
    'ignoreHTTPSErrors': True,
    # todo use env
    'headless': False,
    'defaultViewport': {
        'width': 1980,
        'height': 1060,
    },
    'args': ['--start-maximized'],
}
