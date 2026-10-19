from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator('[data-test="search-query"]')
        self.search_button = page.locator('[data-test="search-submit"]')
        self.product_name = page.locator('[data-test="product-name"]')
        self.search_result = page.locator('[data-test="search_completed"]')
        self.no_results = page.locator('[data-test="no-results"]')
        self.search_reset_button = page.locator('[data-test="search-reset"]')

    def open(self):
        self.page.goto("/")
        expect(self.product_name.first).to_be_visible()

    def search(self, query: str):
        self.search_input.fill(query)
        self.search_button.click()

    def search_reset(self):
        self.search_reset_button.click()