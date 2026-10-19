import pytest

from playwright.sync_api import expect
from pages.home_page import HomePage

def test_search_by_product_name(home_page: HomePage):
    home_page.open()
    home_page.search("Combination Pliers")

    expect(home_page.search_result).to_be_visible()
    expect(home_page.product_name).to_have_text(["Combination Pliers"])


def test_no_results_of_search(home_page: HomePage):
    home_page.open()
    home_page.search("aqa_no_such_product_93847")

    expect(home_page.no_results).to_be_visible()
    expect(home_page.product_name).to_have_count(0)


def test_reset_search(home_page: HomePage):
    home_page.open()
    initial_names = home_page.product_name.all_text_contents()

    home_page.search("Combination Pliers")
    expect(home_page.product_name).to_have_text(["Combination Pliers"])

    home_page.search_reset()
    expect(home_page.product_name).to_have_text(initial_names)
    expect(home_page.search_input).to_have_value("")

@pytest.mark.parametrize("query", ["Pliers", "Hammer"])
def test_search_by_part_of_name(home_page: HomePage, query: str):
    home_page.open()

    home_page.search(query)

    expect(home_page.search_result).to_be_visible()
    expect(home_page.product_name.first).to_be_visible()

    for product in home_page.product_name.all():
        expect(product).to_contain_text(query)