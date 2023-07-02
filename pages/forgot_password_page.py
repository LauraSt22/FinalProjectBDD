from selenium.webdriver.common.by import By
from pages.base_page import Basepage
from time import sleep


class Forgot_Pwd_Page(Basepage):
    EMAIL_INPUT =  (By.XPATH, f'//input[@placeholder="Enter your email"]')
    INVALID_EMAIL_MESSAGE = (By.XPATH, f'//p[contains(text(), "Please enter a valid email address!")]')
    SEND_EMAIL_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]//div/div[2]/button')
    BACK_TO_LOGIN = (By.LINK_TEXT, "Back to login")

    def set_emai(self, email):
        self.wait_for_elem(*self.EMAIL_INPUT)
        self.chrome.find_element(*self.EMAIL_INPUT).click()

    def click_send_email_button(self):
        self.chrome.find_element(*self.SEND_EMAIL_BUTTON).click()

    def click_back_to_login(self):
        self.chrome.find_element(*self.BACK_TO_LOGIN).click()

    def verify_error_email_message(self):
        expected = "Please enter a valid email address!"
        actual = self.chrome.find_element(*self.INVALID_EMAIL_MESSAGE).text
        self.assertEqual(expected, actual, 'The message of the page is incorrect.')

