import json
import requests
import allure


def add_product_to_cart(product_id: int):
    session = requests.Session()
    url = f"https://demowebshop.tricentis.com/addproducttocart/catalog/{product_id}/1/1"
    response = session.post(url)

    # ---------- CONSOLE ----------
    print("\nAPI REQUEST")
    print(f"URL: {url}")
    print(f"STATUS CODE: {response.status_code}")
    print("RESPONSE BODY:")
    print(response.text)

    # ---------- ALLURE ----------
    allure.attach(url, "Request URL", allure.attachment_type.TEXT)
    allure.attach(
        json.dumps(response.json(), indent=4, ensure_ascii=False),
        "Response JSON",
        allure.attachment_type.JSON
    )
    allure.attach(
        response.text,
        "Raw response",
        allure.attachment_type.HTML
    )

    return response, session.cookies
