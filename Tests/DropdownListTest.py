from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.DropdownList import DropdownListPage


class DropdownListTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup Chrome WebDriver
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.get("https://the-internet.herokuapp.com/dropdown")
        cls.driver.implicitly_wait(10)


    def test_find_dropdown_list(self):
        """ Test case to verify if the dropdown list is present on the page. """
        dropdown_list_page = DropdownListPage(self.driver)
        res = dropdown_list_page.find_dropdown_list()
        self.assertEqual(res, True)


    def test_select_option_1(self):
        """ Test case to select the first option from the dropdown list. """
        dropdown_list_page = DropdownListPage(self.driver)
        res = dropdown_list_page.select_option("Option 1")
        self.assertEqual(res, True)


    def test_select_option_2(self):
        dropdown_list_page = DropdownListPage(self.driver)
        res = dropdown_list_page.select_option('Option 2')
        self.assertEqual(res , True)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(DropdownListTest('test_find_dropdown_list'))
    suite.addTest(DropdownListTest('test_select_option_1'))
    suite.addTest(DropdownListTest('test_select_option_2'))
    runner = unittest.TextTestRunner()
    runner.run(suite)