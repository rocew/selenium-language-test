from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_add_to_cart_button_presence(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product_main"))
    )

    time.sleep(30)

    add_to_cart_button = browser.find_elements(
        By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert len(
        add_to_cart_button) > 0, "Add to cart button is not found on the page"

    assert add_to_cart_button[0].is_displayed(
    ), "Add to cart button is not visible"
    assert add_to_cart_button[0].is_enabled(
    ), "Add to cart button is not enabled"
