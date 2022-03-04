from baseapp import BasePage
from selenium.webdriver.common.by import By


class StepikLocators:
    FIRST_NAME_FIELD_LOCATOR = (By.NAME, "first_name")
    LAST_NAME_FIELD_LOCATOR = (By.NAME, "last_name")
    CITY_FIELD_LOCATOR = (By.CSS_SELECTOR, ".city")
    COUNTRY_FIELD_LOCATOR = (By.ID, "country")
    SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[type='submit']")


class StepikPages(BasePage):

    def click_submit_button(self):
        submit_button_locator = self.find_element(StepikLocators.SUBMIT_BUTTON_LOCATOR)
        return submit_button_locator.click()

    def send_keys_to_field(self, locator, value):
        field_locator = self.find_element(locator)
        field_locator.send_keys(value)
