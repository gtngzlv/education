import pytest
from selenium import webdriver


# подготавливаем начальное состояние системы
# декоратор со scope=session означает, что функция выполнится 1 раз за сессию
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    # yield разделяет функцию до тестов и после тестов
    yield driver
    driver.quit()
