from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator('[data-test="search-query"]')
        self.search_button = page.locator('[data-test="search-submit"]')
        self.product_name = page.locator('[data-test="product-name"]')
        self.search_result = page.locator('[data-test="search_completed"]')

    def open(self):
        self.page.goto("/")

    def search(self, query: str):
        self.search_input.fill(query)
        self.search_button.click()