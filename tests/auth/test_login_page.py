"""Example of TestCase for login functionality on dsbot.ru."""
import allure
import pytest

from tests.page import PageObject
from tests.settings import APP_START_URL


@pytest.mark.asyncio
@allure.title('Guest user could use demo-login button')
async def test_login_as_demo_user(new_page: PageObject):
    """Check the functionality of the demo-login to the customer's personal account."""
    with allure.step('Open main application page'):
        await new_page.open(APP_START_URL)

    with allure.step('Click to login page and login as demo-customer'):
        await new_page.goto_login_page()
        await new_page.login_as_demo()

    with allure.step('Customer see his profile with all tabs'):
        assert await new_page.is_authenticated(), 'user is not authenticated'
