from playwright.sync_api import expect
from pages.home_page import HomePage

def test_search_by_product_name(home_page: HomePage):
    home_page.open()
    home_page.search("Combination Pliers")

    expect(home_page.search_result).to_be_visible()
    expect(home_page.product_name).to_have_text(["Combination Pliers"])