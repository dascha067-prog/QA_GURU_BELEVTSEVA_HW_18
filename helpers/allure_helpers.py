import json
import allure


def attach_request(url: str):
    allure.attach(
        url,
        name="Request URL",
        attachment_type=allure.attachment_type.TEXT
    )


def attach_response_json(response):
    allure.attach(
        json.dumps(response.json(), indent=4, ensure_ascii=False),
        name="Response JSON",
        attachment_type=allure.attachment_type.JSON
    )


def attach_raw_response(response):
    allure.attach(
        response.text,
        name="Raw response",
        attachment_type=allure.attachment_type.HTML
    )
