from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Browser:
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    chrome.implicitly_wait(10)
    chrome.set_page_load_timeout(10)
    chrome.maximize_window()

    def close(self):
        self.chrome.close()