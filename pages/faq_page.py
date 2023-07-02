from selenium.webdriver.common.by import By
from pages.base_page import Basepage

class Faq(Basepage):
    FAQ_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[3]/a[1]')
    PRESENT_TEXT = (By.LINK_TEXT, 'Jules FAQ')


    def navigate_to_sign_in_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def click_on_faq(self):
        self.chrome.find_element(*self.FAQ_BUTTON).click()

    def check_page_is_not_empty(self, text_present):
        text_present = self.chrome.find_element(*self.PRESENT_TEXT)
        if text_present.is_displayed():
            print('You can search for the answers')
        else:
            print('The page is not correct')




