from baseapp import BasePage


class StepikPage(BasePage):

    def element_presence(self, text):
        assert self.find_element_by_text(text) == True, "Element was not found"
