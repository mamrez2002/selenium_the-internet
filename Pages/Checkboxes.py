# Checkboxes
# https://the-internet.herokuapp.com/checkboxes

class CheckboxesPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkbox1 = '//*[@id="checkboxes"]/input[1]'
        self.checkbox2 = '//*[@id="checkboxes"]/input[2]'

    def find_checkbox1(self):
        e = self.driver.find_elements('xpath', self.checkbox1)
        return bool(e)

    def find_checkbox2(self):
        e = self.driver.find_elements('xpath', self.checkbox2)
        return bool(e)

    def click_checkbox1(self):
        e = self.driver.find_element('xpath', self.checkbox1)
        before_click = e.is_selected()
        e.click()
        e = self.driver.find_element('xpath', self.checkbox1)
        after_click = e.is_selected()
        return before_click != after_click

    def click_checkbox2(self):
        e = self.driver.find_element('xpath', self.checkbox2)
        before_click = e.is_selected()
        e.click()
        e = self.driver.find_element('xpath', self.checkbox2)
        after_click = e.is_selected()
        return before_click != after_click