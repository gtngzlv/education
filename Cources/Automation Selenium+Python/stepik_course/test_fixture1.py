import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

input_field_locator = ".ember-text-area"
submit_button_locator = ".submit-submission"
correct_message_locator = ".smart-hints__hint"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestStepik:
    s = ""

    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                      "https://stepik.org/lesson/236896/step/1",
                                      "https://stepik.org/lesson/236898/step/1",
                                      "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1",
                                      "https://stepik.org/lesson/236905/step/1"])
    def test_guest_should_see_login_link(self, browser, link):
        answer = math.log(int(time.time()))
        browser.get(link)
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, input_field_locator)),
                                         "Input field element not found")
        input_field = browser.find_element(By.CSS_SELECTOR, input_field_locator)
        input_field.send_keys(str(answer))
        button = browser.find_element(By.CSS_SELECTOR, submit_button_locator)
        button.click()
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, correct_message_locator)),
                                         "Correct message element not found")
        correct_message = browser.find_element(By.CSS_SELECTOR, correct_message_locator)
        assert correct_message.text == "Correct!", self.s + correct_message.text
        return self.s


if __name__ == "__main__":
    print(TestStepik.test_guest_should_see_login_link)
