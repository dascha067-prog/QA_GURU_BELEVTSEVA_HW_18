import allure
from selenium.webdriver.common.by import By

from helpers.api_helpers import add_product_to_cart


@allure.title("Добавление товара в корзину через API с проверкой через UI")
def test_add_product_to_cart_via_api_and_ui(browser):
    response, cookies = add_product_to_cart(product_id=31)

    assert response.status_code == 200
    assert response.json()["success"] is True

    browser.get("https://demowebshop.tricentis.com")
    for cookie in cookies:
        browser.add_cookie({"name": cookie.name, "value": cookie.value})
    browser.refresh()

    browser.find_element(By.CSS_SELECTOR, ".cart-label").click()
    assert len(browser.find_elements(By.CSS_SELECTOR, ".cart-item-row")) > 0
