from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Basepage

class Download_App_Page(Basepage):

    DOWNLOAD_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/div[2]')
    INSTALL_BUTTON = (By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[2]/div[1]/div/div/div/div[1]/div/c-wiz/div/div/div/div/button')
    DISPLAY_MESSAGE_IF_NOT_CONNECTED = (By.LINK_TEXT, 'Pentru a continua, trebuie să te conectezi.')

    def navigate_to_sign_in_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def click_download_for_google(self):
        self.wait_for_elem(*self.DOWNLOAD_BUTTON)
        self.chrome.find_element(*self.DOWNLOAD_BUTTON).click()

    def click_install_button(self):
        self.wait_for_elem(*self.INSTALL_BUTTON)
        self.chrome.find_element(*self.INSTALL_BUTTON).click()

    def check_display_message_if_not_connected(self):
        elem = self.chrome.find_element(*self.DISPLAY_MESSAGE_IF_NOT_CONNECTED)
        if elem.is_displayed():
            print('Please sign in into Google account.')
        else:
            print('No error message to show.')





