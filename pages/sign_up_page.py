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


    def navigate_to_sign_up_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def click_sign_up_button(self):
        self.chrome.find_element(*self.SIGN_UP_BUTTON).click()

    def select_option(self):
        self.chrome.find_element(*self.PERSONAL_BUTTON).click()

    def click_continue_button(self):
        self.wait_for_elem(*self.CONTINUE_BUTTON)
        self.chrome.find_element(*self.CONTINUE_BUTTON).click()
        sleep(1)

    def add_first_name(self):
        self.wait_for_elem(*self.FIRST_NAME_INPUT)
        self.chrome.find_element(*self.FIRST_NAME_INPUT).send_keys('first')
        sleep(1)
        self.chrome.find_element(*self.FIRST_NAME_INPUT).send_keys(Keys.ENTER)

    def add_last_name(self):
        self.wait_for_elem(*self.LAST_NAME_INPUT)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys('last')
        sleep(1)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys(Keys.ENTER)

    def add_email(self):
        self.wait_for_elem(*self.EMAIL_INPUT)
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys('email')

    def verify_display_invalid_email(self):
        actual = self.chrome.find_element(By.XPATH, '/html/body/div/div/div[4]/div[2]/div/div[2]/div/p').is_displayed()
        if actual:
            print('Add a valid email address')
        else:
            print("The email was successfully created! ")

    def add_correct_email(self, email_correct):
        actual = WebDriverWait(self.chrome, 3).until(EC.text_to_be_present_in_element((By.XPATH,f'/html/body/div/div/div[4]/div[2]/div/div[2]/div/p'),
                                                                                      "Please enter a valid email address"))
        if actual:
            email_input = self.chrome.find_element(*self.EMAIL_INPUT)
            email_input.send_keys(Keys.CONTROL + 'a')
            email_input.send_keys(Keys.BACKSPACE)
            self.chrome.find_element(*self.EMAIL_INPUT).send_keys('correct_email')
        else:
            print(f'Displayed the message: email is correct')

    def verify_display_invalid_email(self):
        elem = self.chrome.find_element(By.XPATH, '/html/body/div/div/div[4]/div[2]/div/div[2]/div/p')
        if len(elem) > 0:
            print('There is a message')
        else:
            print('Message does not exist.')

    def verify_url_message(self):
        self.verify_url_message()




