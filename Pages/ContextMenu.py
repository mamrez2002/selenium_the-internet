# Context Menu
# https://the-internet.herokuapp.com/context_menu

from selenium.webdriver import ActionChains
import time

class ContextMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.context_menu_locator = '//*[@id="hot-spot"]'

    def find_context_menu(self):
        e = self.driver.find_elements('xpath', self.context_menu_locator)
        return bool(e)

    def right_click_context_menu(self):
        e = self.driver.find_element('xpath', self.context_menu_locator)
        action = ActionChains(self.driver)
        action.context_click(e).perform()
        a = self.driver.switch_to.alert
        text = a.text
        a.accept()
        return text