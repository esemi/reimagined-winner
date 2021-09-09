import asyncio

import pytest
from pyppeteer import launch
from pyppeteer.browser import Browser

from tests.page import PageObject
from tests.settings import BROWSER_SETTINGS


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
async def new_page(browser: Browser) -> PageObject:
    # todo use CustomPage
    page = PageObject(await browser.newPage())
    yield page
    await page.page.close()
