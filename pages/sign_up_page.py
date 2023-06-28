from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Basepage

class Sign_Up_Page(Basepage):
    SIGN_UP_BUTTON = (By.XPATH, '/html/body/div/div/div[2]/form/div/div[4]/a')
    PERSONAL_BUTTON = (By.XPATH, '/html/body/div/div/div[4]/div[2]/div/div[3]/label/span[1]/span')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[5]/button/span[1]')
    FIRST_NAME_INPUT = (By.XPATH, '/html/body/div/div/div[4]/div[2]/div/div[2]/div/div/input')
    LAST_NAME_INPUT = (By.XPATH, '/html/body/div/div/div[4]/div[2]/div/div[2]/div/div/input')
    EMAIL_INPUT = (By.XPATH, '/html/body/div/div/div[4]/div[2]/div/div[2]/div/div/input')
    MESSAGE_EMAIL_INPUT = (By.XPATH, '/html/body/div/div/div[4]/div[2]/div/div[2]/div/p')
    EMAIL_VALIDATION_ERROR = (By.XPATH,'//div[@id="root"]//p')


    def navigate_to_sign_up_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def click_sign_up_button(self):
        self.chrome.find_element(*self.SIGN_UP_BUTTON).click()

    def select_option(self):
        self.chrome.find_element(*self.PERSONAL_BUTTON).click()

    def click_continue_button(self):
        self.wait_for_elem(*self.CONTINUE_BUTTON)
        self.chrome.find_element(*self.CONTINUE_BUTTON).click()

    def add_first_name(self, first_name):
        self.wait_for_elem(*self.FIRST_NAME_INPUT)
        self.chrome.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.chrome.find_element(*self.FIRST_NAME_INPUT).send_keys(Keys.ENTER)

    def add_last_name(self, last_name):
        self.wait_for_elem(*self.LAST_NAME_INPUT)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys(Keys.ENTER)

    def add_email(self,user_email):
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(user_email)

    def verify_display_invalid_email(self, expected_error_message):
        actual_error = self.chrome.find_element(*self.EMAIL_VALIDATION_ERROR).text
        assert expected_error_message == actual_error,f"Error: Invalid message. expected: {expected_error_message}, actual: {actual_error}"

    def verify_url_message(self):
        self.verify_url_message()




