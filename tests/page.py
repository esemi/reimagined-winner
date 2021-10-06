"""Page elements' locators and selecting tools."""
from dataclasses import fields
from typing import Optional, Tuple

from pyppeteer import errors
from pyppeteer.element_handle import ElementHandle
from pyppeteer.page import Page

from tests.partner.schemas import Partner
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

    async def has_element(self, xpath: str) -> bool:
        """Check element exist on current page."""
        return bool(await self.get_element(xpath))

    async def make_screenshot(self):
        await self._page.screenshot(path='/tmp/tmp.png')



class MainPage(PageObject):
    """Index administrator page."""
    async def goto_partners_page(self) -> 'PartnerPage':
        menu_link = await self.get_element('//a/span[text()="Partners"]')
        assert menu_link, 'partner menu link not found'
        await menu_link.click()
        return await PartnerPage.init(self._page)


class PartnerPage(PageObject):
    """Partners administrator page."""

    async def locate_add_form_button(self) -> Optional[ElementHandle]:
        return await self.get_element('//a[text()="Add Partner"]')

    async def open_add_form(self):
        form_open_button = await self.locate_add_form_button()
        assert form_open_button, 'Add partner button not found'
        await form_open_button.click()

    async def locate_create_form_button(self) -> Optional[ElementHandle]:
        return await self.get_element('//button[@data-action-name="saveAndReturn"]')

    async def locate_create_form_field(
        self,
        name: str,
    ) -> Tuple[Optional[ElementHandle], Optional[ElementHandle]]:
        selector = f'Partner_{name}'
        field_input = await self.get_element(f'//input[@id="{selector}"]')
        field_box = None if not field_input else (await field_input.xpath('./parent::div'))[0]
        return field_input, field_box

    async def locate_create_form_error_text(self, name: str):
        _, box = await self.locate_create_form_field(name)
        return await box.querySelectorEval('div', 'node => node.innerText')

    async def fill_create_form(
        self,
        partner_model: Partner,
    ):
        for field_name in fields(partner_model):
            field, box = await self.locate_create_form_field(str(field_name.name))
            assert field and box, f'Not found "{field_name}" form input'
            await field.type(getattr(partner_model, field_name.name))

        form_create_button = await self.locate_create_form_button()
        assert form_create_button, 'Create partner button not found'
        await form_create_button.click()
