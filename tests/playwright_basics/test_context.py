from playwright.sync_api import Page

def test_pages_share_context(page: Page):
    context = page.context
    second_page = context.new_page()

    assert second_page.context is context


def test_add_cookie(page: Page):
    context = page.context
    context.add_cookies([
        {
            "name": "learning_session",
            "value": "student",
            "url": "https://practicesoftwaretesting.com/",
        }
    ])
    second_page = context.new_page()
    cookies = second_page.context.cookies(
        "https://practicesoftwaretesting.com/"
    )

    assert len(cookies) == 1
    assert cookies[0]["name"] == "learning_session"
    assert cookies[0]["value"] == "student"


def test_cookie_is_isolated_between_contexts(page: Page, new_context):
    context = page.context
    context.add_cookies([
        {"name": "learning_session",
        "value": "student",
        "url": "https://practicesoftwaretesting.com/",}
    ])
    cookies1 = context.cookies(
        "https://practicesoftwaretesting.com/"
    )

    assert len(cookies1) == 1
    assert cookies1[0]["name"] == "learning_session"
    assert cookies1[0]["value"] == "student"

    other_context = new_context()
    page_in_other_context = other_context.new_page()
    cookies2 = page_in_other_context.context.cookies(
        "https://practicesoftwaretesting.com/"
    )

    assert len(cookies2) == 0