import pytest
from playwright.sync_api import Page, expect


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


def test_check_size_in_stock(page: Page):
    # Make sure we're at the right product page
    expect(page.get_by_role("heading", name="Skinny Traveler Pant")).to_be_visible()

    # Choose the pants color: Black
    page.get_by_label("Black", exact=True).check()

    # Click on waist size "32W" NOTE: when out of stock, the label = "Size:32W out of stock" so using exact=False
    page.get_by_label("Size:32W", exact=False).click()

    # Click on length size "30L" NOTE: when out of stock, the label = "Size:30L out of stock" so using exact=False
    page.get_by_label("Size:30L", exact=False).click()

    # Now that the desired size is selected, determine if it's in stock
    # 'Add to Bag' button will be disabled if it's not in stock NOTE: the label is a long sentence so using exact=False
    if page.get_by_label("Add to bag", exact=False).is_enabled():
        print("In stock!")
        assert True
    else:
        print("Out of stock!")
        assert False
