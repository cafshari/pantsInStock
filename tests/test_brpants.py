import pytest
import os
from playwright.sync_api import Page, expect


def test_check_product_header(page: Page):
    # Make sure we're at the right product page
    expect(page.get_by_role("heading", name="Skinny Traveler Pant")).to_be_visible()


def test_check_size_in_stock(page: Page):
    # Choose the pants color: Black
    page.get_by_label("Black", exact=True).check()

    # Click on waist size "32W" NOTE: when out of stock, the label = "Size:32W out of stock" so using exact=False
    page.get_by_label("Size:32W", exact=False).click()

    # Click on length size "30L" NOTE: when out of stock, the label = "Size:30L out of stock" so using exact=False
    page.get_by_label("Size:30L", exact=False).click()

    # Now that the desired size is selected, determine if it's in stock
    # 'Add to Bag' button will be disabled if it's not in stock NOTE: the label is a long sentence so using exact=False
    env_file = os.getenv('GITHUB_ENV')  # will result in env_file = None if run locally
    if page.get_by_label("Add to bag", exact=False).is_enabled():
        print("In stock!")
        if env_file:
            with open(env_file, "a") as myfile:
                myfile.write(f"IS_IN_STOCK=true")
    else:
        print("Out of stock!")
        if env_file:
            with open(env_file, "a") as myfile:
                myfile.write(f"IS_IN_STOCK=false")
