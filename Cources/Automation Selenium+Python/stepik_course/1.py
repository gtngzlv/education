from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))


price = "id"

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = browser.find_element(By.ID, "book")
text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()

x = browser.find_element(By.ID, "input_value")
browser.execute_script("arguments[0].scrollIntoView(true);", x)
x_calc=str(calc(int(x.text)))

input_field=browser.find_element(By.ID, "answer")
input_field.send_keys(x_calc)
browser.find_element(By.ID, "solve").click()


