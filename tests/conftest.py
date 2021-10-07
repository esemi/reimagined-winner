"""Basic fixtures for all UI-tests."""

import asyncio

import pytest
from pyppeteer import launch
from pyppeteer.browser import Browser

from tests.page import PageObject
from tests.partner.partner_page import PartnerPage
from tests.settings import BROWSER_SETTINGS, APP_START_URL, CLEAR_DB_URL


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
async def main_page(browser: Browser):  # noqa: WPS442
    page = await MainPage.init(await browser.newPage())
    await page.open(CLEAR_DB_URL)
    await page.open(APP_START_URL)
    yield page
    await page.close()


class MainPage(PageObject):
    """Index administrator page."""

    async def goto_partners_page(self) -> 'PartnerPage':
        menu_link = await self.get_element('//a/span[text()="Partners"]')
        assert menu_link, 'partner menu link not found'
        await menu_link.click()
        return await PartnerPage.init(self._page)
