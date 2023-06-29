from selenium.webdriver.common.by import By
from pages.base_page import Basepage

class Download_App_For_Apple(Basepage):
    DOWNLOAD_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/div[1]/a')
    MESSAGE_DISPLAYED = (By.XPATH, '/html/body/div[3]/main/div[2]/div/div')

    def navigate_to_sign_in_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def click_download_for_apple(self):
        self.wait_for_elem(*self.DOWNLOAD_BUTTON)
        self.chrome.find_element(*self.DOWNLOAD_BUTTON).click()

    def message_displayed_to_get_the_app(self):
        message = self.chrome.find_element(*self.MESSAGE_DISPLAYED)
        if message.is_displayed():
            print('Follow the instructions')
        else:
            print('There is no message')


