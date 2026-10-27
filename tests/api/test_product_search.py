import requests
import pytest

REQUEST_TIMEOUT = 10

def test_search_by_product_name():
    response = requests.request(
        method="QUERY",
        url="https://api.practicesoftwaretesting.com/products/search",
        json={"q": "Combination Pliers"},
        timeout=REQUEST_TIMEOUT
    )

    assert response.status_code == 200

    body = response.json()

    assert body["total"] == 1
    assert len(body["data"]) == 1
    assert body["data"][0]["name"] == "Combination Pliers"

def test_search_with_no_results():
    response = requests.request(
        method="QUERY",
        url="https://api.practicesoftwaretesting.com/products/search",
        json={"q": "aqa_no_such_product_93847"},
        timeout=REQUEST_TIMEOUT
    )

    assert response.status_code == 200

    body = response.json()

    assert body["total"] == 0
    assert body["data"] == []

@pytest.mark.parametrize("query", ["Pliers", "Hammer"])
def test_search_by_partial_product_name(query: str):
    response = requests.request(
        method="QUERY",
        url="https://api.practicesoftwaretesting.com/products/search",
        json={"q": query},
        timeout=REQUEST_TIMEOUT
    )
    assert response.status_code == 200

    body = response.json()

    assert body["total"] > 0
    assert len(body["data"]) > 0

    for product in body["data"]:
        assert query in product["name"]