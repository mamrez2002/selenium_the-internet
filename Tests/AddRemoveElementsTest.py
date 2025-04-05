from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.AddRemoveElements import AddRemoveElementsPage


class AddRemoveElementsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup Chrome WebDriver
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        cls.driver.implicitly_wait(10)


    def test_find_add_element(self):
        """ Test case to verify if the 'Add Element' button is present on the page."""
        add_remove_page = AddRemoveElementsPage(self.driver)
        res = add_remove_page.find_add_element()
        self.assertEqual(res, True)

    def test_click_add_element(self):
        """ Test case to verify adding an element using the 'Add Element' button. """
        add_remove_page = AddRemoveElementsPage(self.driver)
        res = add_remove_page.click_add_element()
        self.assertEqual(res,True)
        time.sleep(1)

    def test_click_delete_element(self):
        add_remove_page = AddRemoveElementsPage(self.driver)
        res = add_remove_page.click_delete_element()
        self.assertEqual(res, True)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # Close the browser after tests
        cls.driver.quit()


if __name__ == "__main__" :
    suite = unittest.TestSuite()
    suite.addTest(AddRemoveElementsTest('test_find_add_element'))
    suite.addTest(AddRemoveElementsTest('test_click_add_element'))
    suite.addTest(AddRemoveElementsTest('test_click_delete_element'))
    unittest.TextTestRunner().run(suite)

