"""Example of TestCase for login functionality on dsbot.ru."""

import allure
import pytest

from tests.form_utils import BLANK_SYMBOL
from tests.page import PartnerPage
from tests.partner.schemas import Partner


@pytest.mark.asyncio
@allure.title('Admin try create empty partner.')
async def test_required_fields(partner_page: PartnerPage):
    with allure.step('Fill in the new partner form without data'):
        await partner_page.open_add_form()

        empty_partner = Partner(
            **{name: BLANK_SYMBOL for name in Partner.required_fields()}
        )
        await partner_page.fill_create_form(empty_partner)

    with allure.step('Partner was not added and form display errors'):
        assert await partner_page.locate_create_form_button(), 'create form button not found'
        for name in Partner.required_fields():
            error_message = await partner_page.locate_create_form_error_text(name)
            assert 'This value should not be blank' in error_message, \
                f'create form field {name} does not have error message'


# @pytest.mark.asyncio
# @allure.title('Admin can add a partner to the system.')
# async def test_happy_path(partner_page: PartnerPage):
#     # todo clear db before
#     with allure.step('Fill in the new partner form with the correct data'):
#         await partner_page.open_add_form()
#         await partner_page.fill_create_form(
#             # todo impl
#         )
#
#     with allure.step('Partner was added successfully'):
#         assert not await partner_page.locate_create_form_button(), 'create form button found'
#         # todo assert await partner_page.partner_exist_in_list(partner_id), 'partner not found in list'