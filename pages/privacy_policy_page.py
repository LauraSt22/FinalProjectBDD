from selenium.webdriver.common.by import By
from pages.base_page import Basepage

class Privacy_Policy(Basepage):

    PRIVACY_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[3]/a[3]')
    WRITING = (By.LINK_TEXT,'Privacy Policy')

    def navigate_to_sign_in_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def click_on_privacy(self):
        self.chrome.find_element(*self.PRIVACY_BUTTON).click()
        
    def check_wrinting(self, text_present):
        text_present = self.chrome.find_element(*self.WRITING)
        if text_present.is_displayed():
            print('You can read the privacy policy')
        else:
            print('The page is not correct')



