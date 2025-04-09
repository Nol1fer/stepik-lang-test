from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_present(browser):
    browser.get(link)
    browser.implicitly_wait(10)

    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert (
        add_to_basket_button is not None
    ), "Add to Basket button not found on the page"
