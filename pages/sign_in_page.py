from selenium.webdriver.common.by import By
from pages.base_page import Basepage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver import Keys
#sectiune de identificare a elementelor
class Sign_In_Page(Basepage):


    EMAIL_INPUT = (By.XPATH, f'//input[@placeholder="Enter your email"]')
    PWD_INPUT = (By.XPATH, f'//input[@placeholder="Enter your password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    FORGOT_PWD = (By.LINK_TEXT, 'Forgot password?')
    # MESSAGE_INPUT_CORRECT_MESSAGE = ('/html/body/div/div/div[2]/form/div/div[2]/div/p')


    def navigate_to_sign_in_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def set_email(self, email):
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_pwd(self, pwd):
        self.chrome.find_element(*self.PWD_INPUT).send_keys(pwd)
        pwd_input = self.chrome.find_element(*self.PWD_INPUT)
        pwd_input.send_keys(Keys.CONTROL + 'a')
        pwd_input.send_keys(Keys.BACKSPACE)

    def click_login_button(self):
        self.wait_for_elem(*self.LOGIN_BUTTON)
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def click_fogot_pwd_link(self):
        self.chrome.find_element(*self.FORGOT_PWD).click()



    def check_display_invalid_email(self):
        elem = self.chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/p').is_displayed()
        if len(elem) > 0:
            print('Message exists.')
        else:
            print('Message does not exist.')

    def check_enable_button(self):
        login_button = self.chrome.find_element(By.XPATH, '//button[@type="submit"]')
        if login_button:
            print('Login button is enabled.')
        else:
            print('Login button is disabled.')

    def verify_display_invalid_message(self):
        elem = self.chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div/p')
        if elem.is_displayed():
            print('There is a message')
        else:
            print('Message does not exist.')

    # def verify_display_invalid_message(self):
    #     actual = self.chrome.find_element(*self.MESSAGE_INPUT_CORRECT_MESSAGE)
    #     expected = "Please enter a valid email address!"
    #     self.assertEqual(expected, actual, 'The message of the page is incorrect.')






    
