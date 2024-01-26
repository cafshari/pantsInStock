import re

import pytest
from playwright.sync_api import Page, expect


def open_page(page: Page) -> None:
    page.goto("https://bananarepublic.gap.com/browse/product.do?pid=2666360923230")


def close_dynamic_modals(page: Page) -> None:
    if page.get_by_test_id("dynamic-modal-content"):
        print('closing email sign up modal')
        page.get_by_label("close email sign up modal").click()  # this label is used for multiple different modals

    if page.get_by_label("Close Survey", exact=True):
        print('closing survey modal')
        page.get_by_label("Close Survey", exact=True).click()


# this fixture will run before every test
@pytest.fixture(scope="function", autouse=True)
def start(page: Page):
    open_page(page)
    close_dynamic_modals(page)


def test_check_size_in_stock(page: Page):
    # Choose the pants color: Black
    page.get_by_label("Black", exact=True).check()

    # First, click on waist size "32W" NOTE: when out of stock, the label = "Size:32W out of stock" so using exact=False
    page.get_by_label("Size:32W", exact=False).click()

    # Then, click on length size "30L" NOTE: when out of stock, the label = "Size:30L out of stock" so using exact=False
    page.get_by_label("Size:30L", exact=False).click()

    # Now that the desired size is selected, determine if it's in stock
    # 'Add to Bag' button will be disabled if it's not in stock NOTE: the label is a long sentence so using exact=False
    if page.get_by_label("Add to bag", exact=False).is_enabled():
        print("your size is in stock!")
    else:
        print("your size is out of stock.")

