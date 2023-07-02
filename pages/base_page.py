from browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest

class Basepage(Browser, unittest.TestCase):
    def wait_for_elem(self, by, selector):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((by, selector)))

<<<<<<< HEAD
    def check_current_url(self, expected_url):
        actual_url = self.chrome.current_url
        self.assertEqual(actual_url, expected_url, "The URL doesn't match.")
=======
    def check_current_url(self,expected_url):
        actual_url = self.chrome.current_url
        self.assertEqual(actual_url,expected_url, "The URL doesn't match.")
>>>>>>> origin/master
