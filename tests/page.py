"""Page elements' locators and selecting tools."""
from typing import Optional, List

from pyppeteer import errors
from pyppeteer.element_handle import ElementHandle
from pyppeteer.page import Page

from tests.settings import SEARCH_ELEMENT_TIMEOUT


class PageObject:
    """Basic page locators and selecting methods."""

    def __init__(self, page: Page):
        self._page = page

    @classmethod
    async def init(cls, page: Page):
        # temporary auth for test environment only
        await page.setExtraHTTPHeaders({
            'Authorization': 'Basic NHRoZGltOnY0bHRpY2Vl',
        })
        return cls(page)

    async def close(self):
        if not self._page.isClosed():
            await self._page.close()

    async def open(self, url: str):
        """Open url in tab."""
        await self._page.goto(url)

    async def get_element(self, xpath: str) -> Optional[ElementHandle]:
        """Search element on current page w/ timeout."""
        try:
            # todo colored found elem
            return await self._page.waitForXPath(xpath, visible=True, timeout=SEARCH_ELEMENT_TIMEOUT)
        except (errors.PageError, errors.TimeoutError):
            return None

    async def get_elements(self, xpath: str) -> List[ElementHandle]:
        return await self._page.xpath(xpath)

    async def get_element_content(self, elem: ElementHandle) -> str:
        return await self._page.evaluate('node => node.innerText', elem)

    async def has_element(self, xpath: str) -> bool:
        """Check element exist on current page."""
        return bool(await self.get_element(xpath))
