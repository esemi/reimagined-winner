import pytest
from pyppeteer.page import Page

from tests.conftest import APP_HOST


@pytest.mark.asyncio
async def test_not_found(new_page: Page):
    """Check login button was exists."""

    await new_page.goto(APP_HOST)
    # todo use CustomPage
    assert await new_page.waitForXPath('//a[contains(text(),"sdsd")]', visible=True, timeout=5000), 'sdsdsdsd'


