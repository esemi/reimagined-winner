"""Partner page and elements' locators."""

from dataclasses import fields
from typing import Optional, Tuple, List

from pyppeteer.element_handle import ElementHandle

from tests.page import PageObject
from tests.partner.schemas import Partner


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

    async def locate_partners_list(self) -> List[ElementHandle]:
        await self.has_element('//section[@id="main"]')
        return await self.get_elements('//section[@id="main"]//tr[@data-id]')

    async def partner_list_row_to_text(self, elem: ElementHandle) -> str:
        columns = await elem.xpath('.//td[@data-label]//span')
        nodes = [await self.get_element_content(el) for el in columns]
        return '\n'.join(nodes)
