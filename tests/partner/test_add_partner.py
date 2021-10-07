"""TestCase for create partner functionality."""
import uuid

import allure
import pytest

from tests.form_utils import BLANK_SYMBOL
from tests.partner.partner_page import PartnerPage
from tests.partner.schemas import Partner


@pytest.mark.asyncio
@allure.title('Admin try create empty partner.')
async def test_required_fields(partner_page: PartnerPage):
    with allure.step('Fill in the new partner form without data'):
        await partner_page.open_add_form()

        empty_partner = Partner(
            **{name: BLANK_SYMBOL for name in Partner.required_fields()},
        )
        await partner_page.fill_create_form(empty_partner)

    with allure.step('Partner was not added and form display errors'):
        assert await partner_page.locate_create_form_button(), 'create form button not found'
        for name in Partner.required_fields():
            error_message = await partner_page.locate_create_form_error_text(name)
            assertion_error = f'create form field {name=} does not have error message'
            assert error_message and 'This value should not be blank' in error_message, assertion_error


@pytest.mark.asyncio
@allure.title('Admin can add a partner to the system.')
async def test_happy_path(partner_page: PartnerPage, valid_partner_cf: str):
    uniq_partner_uid = uuid.uuid4().hex
    with allure.step('Fill in the new partner form with the correct data'):
        await partner_page.open_add_form()
        await partner_page.fill_create_form(Partner(
            descrizione=f'autotest descrizione example {uniq_partner_uid}',
            indirizzo='autotest indirizzo example',
            comune='autotest comune example',

            cap='12345',
            provincia='AA',
            cf=valid_partner_cf,
        ))

    with allure.step('Partner was added successfully'):
        assert not await partner_page.locate_create_form_button(), 'create form button found'
        partner_rows = await partner_page.locate_partners_list()
        assert len(partner_rows), 'Not found partners on table'

        partner_as_text = await partner_page.partner_list_row_to_text(partner_rows[0])
        assert uniq_partner_uid in partner_as_text, f'Not found partner {uniq_partner_uid} in first table row'
