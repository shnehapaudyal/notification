import unittest
from selenium import webdriver


class BrowserRunner(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://dev-dot-lightspeed-cms.lax-hamrostack.com')
        self.assertIn("Light Speed", self.driver.title)

    # def tearDown(self):
    #     self.driver.close()
