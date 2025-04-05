# Add/Remove Elements
# https://the-internet.herokuapp.com/add_remove_elements/


class AddRemoveElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_element_button = '//*[@id="content"]/div/button'
        self.delete_button = '//*[@id="elements"]/button'

    def find_add_element(self):
        e = self.driver.find_elements('xpath', self.add_element_button)
        return bool(e)

    def click_add_element(self):
        self.driver.find_element('xpath',self.add_element_button).click()
        e = self.driver.find_elements('xpath',self.delete_button)
        return bool(e)


    def click_delete_element(self):
        self.driver.find_element('xpath',self.delete_button).click()
        e = self.driver.find_elements('xpath', self.delete_button)
        return not bool(e)