from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import Basepage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Terms_And_Conditions(Basepage):

    TERMS_AND_CONTITIONS_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[3]/a[2]')
    LINK_BUTTON = (By.XPATH, '/html/body/section/ol/li[5]/a')

    def navigate_to_sign_in_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def click_terms_conditions_button(self):
        self.chrome.find_element(*self.TERMS_AND_CONTITIONS_BUTTON).click()

    def click_on_link(self):
        self.wait_for_elem(*self.LINK_BUTTON)
        self.chrome.find_element(*self.LINK_BUTTON).click()

    def verify_url(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://static.jules.app/terms_of_use.html'
        self.assertEqual(actual_url, expected_url, "The URL doesn't match.")
