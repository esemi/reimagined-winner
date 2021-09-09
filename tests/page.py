from typing import Optional, Any

from pyppeteer import errors
from pyppeteer.page import Page


class PageObject:
    def __init__(self, page: Page):
        self.page = page

    async def open(self, url: str):
        await self.page.goto(url)

    async def get_element(self, xpath: str) -> Optional[Any]:
        try:
            return await self.page.waitForXPath(xpath, visible=True, timeout=5000)
        except (errors.PageError, errors.TimeoutError):
            return None

    async def has_element(self, xpath: str) -> bool:
        return bool(await self.get_element(xpath))

    async def goto_login_page(self):
        """Go to login page."""
        login_link = await self.get_element('//a[contains(text(),"вход")]')
        assert login_link, 'login link was not found'
        await login_link.click()

    async def login_as_demo(self):
        """Login as demo-customer."""
        demo_link = await self.get_element('//a[contains(text(),"Демо вход")]')
        assert demo_link, 'login as demo link was not found'
        await demo_link.click()

    async def is_authenticated(self) -> bool:
        """Customer is authenticated now."""
        return all([
            await self.has_element('//a[contains(text(), "выйти")]'),
            await self.has_element('//a[contains(text(), "профиль")]'),
            await self.has_element('//a[contains(text(), "списания")]'),
            await self.has_element('//a[contains(text(), "сообщения")]'),
            await self.has_element('//a[contains(text(), "проверки")]'),
            await self.has_element('//div[@id="player-main"]'),
        ])
