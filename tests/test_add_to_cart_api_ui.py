import json
import requests
import allure
from allure import step
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Добавление товара №13 в корзину через API с проверкой через UI")
def test_add_product_13_to_cart_via_api_and_ui():
    with step("API Request"):
        response = requests.post(
            "https://demowebshop.tricentis.com/addproducttocart/catalog/13/1/1"
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

        allure.attach(
            json.dumps(response.json(), indent=4, ensure_ascii=False),
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )

    with step("UI: Открыть сайт и корзину"):
        driver = webdriver.Chrome()
        driver.get("https://demowebshop.tricentis.com")
        driver.find_element(By.CSS_SELECTOR, ".cart-label").click()

        assert "shopping cart" in driver.title.lower()
        driver.quit()


@allure.title("Добавление товара №31 в корзину через API с проверкой через UI")
def test_add_product_31_to_cart_via_api_and_ui():
    # ---------- API ----------
    with step("API Request"):
        url = "https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1"
        response = requests.post(url)

        # ЛОГИРОВАНИЕ В КОНСОЛЬ
        print("API REQUEST:")
        print(f"URL: {url}")
        print(f"STATUS CODE: {response.status_code}")
        print("RESPONSE BODY:")
        print(response.text)

        # Allure: запрос инфы
        allure.attach(
            url,
            name="Request URL",
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            str(response.status_code),
            name="Response status code",
            attachment_type=allure.attachment_type.TEXT
        )

        # Allure: ответ
        allure.attach(
            json.dumps(
                {
                    "success": response.json().get("success"),
                    "message_preview": response.json().get("message")[:200]
                },
                indent=4,
                ensure_ascii=False
            ),
            name="Response JSON (parsed)",
            attachment_type=allure.attachment_type.JSON
        )

        # Allure: ответ (HTML внутри JSON)
        allure.attach(
            response.text,
            name="Raw response (HTML)",
            attachment_type=allure.attachment_type.HTML
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

        # ---------- UI ----------
    with step("UI: Открыть сайт и страницу корзины"):
        driver = webdriver.Chrome()
        driver.get("https://demowebshop.tricentis.com")
        driver.find_element(By.CSS_SELECTOR, ".cart-label").click()

        assert "shopping cart" in driver.title.lower()

        driver.quit()