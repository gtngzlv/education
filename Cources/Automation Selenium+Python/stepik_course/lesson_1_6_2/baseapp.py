from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_web_page(self):
        self.driver.get(self.url)

    def crypted_text(self):
        return str(math.ceil(math.pow(math.pi, math.e) * 10000))

    def find_element_by_text(self, text):
        self.driver.find_element_by_link_text(text)
