from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.ContextMenu import ContextMenuPage

class ContextMenuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup Chrome WebDriver
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.get("https://the-internet.herokuapp.com/context_menu")
        cls.driver.implicitly_wait(10)

    def test_find_context_menu(self):
        """ Test case to verify if the context menu is present on the page. """
        context_menu_page = ContextMenuPage(self.driver)
        res = context_menu_page.find_context_menu()
        self.assertEqual(res, True)

    def test_right_click_context_menu(self):
        """ Test case to perform right click on the context menu and accept the alert. """
        context_menu_page = ContextMenuPage(self.driver)
        alert_text = context_menu_page.right_click_context_menu()
        # Verify the alert text
        self.assertEqual(alert_text, "You selected a context menu")
        time.sleep(1)


    @classmethod
    def tearDownClass(cls):
        # Close the browser after tests
        cls.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ContextMenuTest('test_find_context_menu'))
    suite.addTest(ContextMenuTest('test_right_click_context_menu'))
    runner = unittest.TextTestRunner()
    runner.run(suite)