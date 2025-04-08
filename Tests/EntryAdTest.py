from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.EntryAd import  EntryAdPage


class EntryAdTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup Chrome WebDriver
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.get("https://the-internet.herokuapp.com/entry_ad")
        cls.driver.implicitly_wait(10)

    def test_find_entry_ad(self):
        """ Test case to verify if the entry ad is present on the page. """
        entry_ad_page = EntryAdPage(self.driver)
        res = entry_ad_page.find_entry_ad()
        self.assertEqual(res, True)

    def test_close_entry_ad(self):
        """ Test case to close the entry ad. """
        entry_ad_page = EntryAdPage(self.driver)
        res = entry_ad_page.close_entry_ad()
        self.assertEqual(res, True)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(EntryAdTest('test_find_entry_ad'))
    suite.addTest(EntryAdTest('test_close_entry_ad'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
