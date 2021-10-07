"""Partner-specific fixtures."""

import random

import pytest


@pytest.fixture()
def valid_partner_cf() -> str:
    return random.choice([  # noqa: S311
        '02000000006',
        '02000000014',
        '02000000022',
        '02000000030',
    ])


@pytest.fixture()
@pytest.mark.asyncio
async def partner_page(main_page):
    page = await main_page.goto_partners_page()
    yield page
    await page.close()
