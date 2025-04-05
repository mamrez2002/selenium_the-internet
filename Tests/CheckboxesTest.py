from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.Checkboxes import CheckboxesPage


class CheckboxesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup Chrome WebDriver
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.get("https://the-internet.herokuapp.com/checkboxes")
        cls.driver.implicitly_wait(10)

    def test_find_checkbox1(self):
        """ Test case to verify if checkbox 1 is present on the page. """
        checkboxes_page = CheckboxesPage(self.driver)
        res = checkboxes_page.find_checkbox1()
        self.assertEqual(res, True)

    def test_find_checkbox2(self):
        """ Test case to verify if checkbox 2 is present on the page. """
        checkboxes_page = CheckboxesPage(self.driver)
        res = checkboxes_page.find_checkbox2()
        self.assertEqual(res, True)

    def test_click_checkbox1(self):
        """ Test case to click checkbox 1. """
        checkboxes_page = CheckboxesPage(self.driver)
        res = checkboxes_page.click_checkbox1()
        self.assertEqual(res, True)
        time.sleep(1)

    def test_click_checkbox2(self):
        """ Test case to click checkbox 2. """
        checkboxes_page = CheckboxesPage(self.driver)
        res = checkboxes_page.click_checkbox2()
        self.assertEqual(res, True)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # Close the browser after tests
        cls.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CheckboxesTest('test_find_checkbox1'))
    suite.addTest(CheckboxesTest('test_find_checkbox2'))
    suite.addTest(CheckboxesTest('test_click_checkbox1'))
    suite.addTest(CheckboxesTest('test_click_checkbox2'))
    unittest.TextTestRunner().run(suite)



