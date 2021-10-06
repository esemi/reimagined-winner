"""Basic fixtures for all UI-tests."""

import asyncio

import pytest
from pyppeteer import launch
from pyppeteer.browser import Browser

from tests.page import MainPage, PartnerPage
from tests.settings import BROWSER_SETTINGS, APP_START_URL


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
async def main_page(browser: Browser) -> MainPage:
    page = await MainPage.init(await browser.newPage())
    await page.open(APP_START_URL)
    yield page
    await page.close()


@pytest.fixture()
@pytest.mark.asyncio
async def partner_page(main_page) -> PartnerPage:
    page = await main_page.goto_partners_page()
    yield page
    await page.close()
