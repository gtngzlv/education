from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_language_browser(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_basket_locator = ".btn-add-to-basket"
    assert WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, add_to_basket_locator)),
                                            "Add to basket button not found") is not None, "Add to basket not found"
    time.sleep(30)
