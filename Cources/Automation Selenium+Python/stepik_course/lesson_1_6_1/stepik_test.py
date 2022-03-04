from stepik_pages import StepikPages
from stepik_pages import StepikLocators
import time

first_name_value = "Ivan"
last_name_value = "Ivanov"
city_value = "Moscow"
country_value = "Russia"
link = "http://suninjuly.github.io/simple_form_find_task.html"


def test_stepik(browser):
    stepik_page = StepikPages(browser, link)
    stepik_page.open_website()
    stepik_page.send_keys_to_field(StepikLocators.FIRST_NAME_FIELD_LOCATOR, first_name_value)
    stepik_page.send_keys_to_field(StepikLocators.LAST_NAME_FIELD_LOCATOR, last_name_value)
    stepik_page.send_keys_to_field(StepikLocators.CITY_FIELD_LOCATOR, city_value)
    stepik_page.send_keys_to_field(StepikLocators.COUNTRY_FIELD_LOCATOR, country_value)
    stepik_page.click_submit_button()
    time.sleep(30)
