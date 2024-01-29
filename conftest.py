import pytest
from playwright.sync_api import Page


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.6261.6 Safari/537.36',
        # user agents for playwright listed at: https://github.com/microsoft/playwright/blob/main/packages/playwright
        # -core/src/server/deviceDescriptorsSource.json
        'base_url': 'https://bananarepublic.gap.com'

    }


def open_page(page: Page) -> None:
    page.goto("/browse/product.do?pid=2666360923230")  # base url provided in pytest.ini


def close_dynamic_modals(page: Page) -> None:
    if page.get_by_test_id("dynamic-modal-content").is_visible():
        print('closing promotional modal')
        page.get_by_label("close email sign up modal").click()  # this label is used for multiple different modals

    if page.get_by_label("Close Survey", exact=True).is_visible():
        print('closing survey modal')
        page.get_by_label("Close Survey", exact=True).click()


# this fixture will run before every test
@pytest.fixture(scope="function", autouse=True)
def start(page: Page):
    open_page(page)
    close_dynamic_modals(page)
