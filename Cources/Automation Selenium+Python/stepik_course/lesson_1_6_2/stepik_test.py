from stepik_pages import StepikPage

link = "http://suninjuly.github.io/find_link_text"


def test_stepikpage(browser):
    stepik_page = StepikPage(browser, link)
    stepik_page.open_web_page()
    number = stepik_page.crypted_text()
    stepik_page.find_element_by_text(number)