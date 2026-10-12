from playwright.sync_api import Page, expect

def test_home_page__is_openned(page: Page):
    page.goto("/")
    expect(page.get_by_role("heading", name="Practice Software Testing - Toolshop")).to_be_visible()