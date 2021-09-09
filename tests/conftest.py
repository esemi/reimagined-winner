import asyncio
from typing import Tuple

import pytest
from pyppeteer import launch
from pyppeteer.browser import Browser
from pyppeteer.page import Page


# todo use Path
APP_HOST = 'https://dsbot.ru/'
BROWSER_SETTINGS = {
    'ignoreHTTPSErrors': True,
    'headless': False,
    'defaultViewport': {
        'width': 2560,
        'height': 1440,
    },
    'args': ['--start-maximized'],
}


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
@pytest.mark.asyncio
async def browser() -> Browser:
    browser = await launch(**BROWSER_SETTINGS)
    yield browser
    await browser.close()


@pytest.fixture()
@pytest.mark.asyncio
async def new_page(browser: Browser) -> Page:
    # todo use CustomPage
    page = await browser.newPage()
    yield page
    await page.close()

