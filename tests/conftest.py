"""Basic fixtures for all UI-tests."""

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
    instance = await launch(**BROWSER_SETTINGS)
    yield instance
    await instance.close()


@pytest.fixture()
@pytest.mark.asyncio
async def new_page(browser: Browser) -> PageObject:  # type: ignore   # noqa: WPS442
    page = PageObject(await browser.newPage())
    yield page
    await page.page.close()
