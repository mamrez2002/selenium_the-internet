# Entry Ad
# https://the-internet.herokuapp.com/entry_ad

import time


class EntryAdPage:
    def __init__(self, driver):
        self.driver = driver
        self.entry_ad_locator = '//*[@id="modal"]/div[2]'
        self.close_button_locator = '//*[@id="modal"]/div[2]/div[3]/p'

    def find_entry_ad(self):
        e = self.driver.find_elements('xpath', self.entry_ad_locator)
        return bool(e)

    def close_entry_ad(self):
        e = self.driver.find_element('xpath', self.close_button_locator)
        e.click()
        return True