# Dropdown List
# https://the-internet.herokuapp.com/dropdown

from selenium.webdriver.support.ui import Select

class DropdownListPage:
    def __init__(self, driver):
        self.driver = driver
        self.dropdown_locator = '//*[@id="dropdown"]'

    def find_dropdown_list(self):
        e = self.driver.find_elements('xpath', self.dropdown_locator)
        return bool(e)

    def select_option(self, value):
        e = self.driver.find_element('xpath', self.dropdown_locator)
        select = Select(e)
        select.select_by_visible_text(value)
        res = select.all_selected_options[0].text
        return res == value