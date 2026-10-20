from playwright.sync_api import Page, expect

def test_locator_can_be_created_before_navigation(page: Page):
    search_input = page.locator('[data-test="search-query"]')

    page.goto("/")

    expect(search_input).to_be_visible()
    search_input.fill("Pliers")
    expect(search_input).to_have_value("Pliers")


def test_product_price_belongs_to_selected_card(page: Page):
    page.goto("/")

    cards = page.locator('a[data-test^="product-"]')
    card = cards.filter(
        has=page.get_by_role("heading", name="Pliers", exact=True)
    )
    expect(card).to_have_count(1)

    price = card.locator('[data-test="product-price"]')
    expect(price).to_be_visible()