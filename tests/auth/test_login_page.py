"""Example of TestCase for login functionality on dsbot.ru."""

import pytest

from tests.page import PageObject
from tests.settings import APP_START_URL


@pytest.mark.asyncio
async def test_login_as_demo_user(new_page: PageObject):
    """Check the functionality of the demo-login to the customer's personal account."""
    await new_page.open(APP_START_URL)

    await new_page.goto_login_page()
    await new_page.login_as_demo()

    assert await new_page.is_authenticated(), 'user is not authenticated'
