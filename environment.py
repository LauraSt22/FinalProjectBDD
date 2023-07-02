# o cutiuta care contine cate un obiect de tipul fiecarei clase de pagini
# de fiecare data cand adaugam cate o pagina noua in proiect, aceasta va trebui adaugata si in context
# before_all = nume de metoda standardizat care da sistemului informatii ca
# acele instructiuni trebuie executate inainte de executarea unui scenariu

from pages.sign_in_page import Sign_In_Page
from browser import  Browser
from pages.forgot_password_page import Forgot_Pwd_Page
from pages.sign_up_page import Sign_Up_Page
from pages.download_app_page import Download_App_Page
from pages.terms_and_conditions_page import Terms_And_Conditions
from pages.download_app_for_apple_pages import Download_App_For_Apple
from pages.faq_page import Faq
from pages.privacy_policy_page import Privacy_Policy


def before_all(context):
    context.browser = Browser()
    context.sign_in_page = Sign_In_Page()
    context.forgot_pass = Forgot_Pwd_Page()
    context.sign_up_page = Sign_Up_Page()
    context.download_app = Download_App_Page()
    context.terms_and_conditions = Terms_And_Conditions()
    context.download_app_for_apple = Download_App_For_Apple()
    context.faq = Faq()
    context.privacy_policy = Privacy_Policy()


def after_all(context):
    context.browser.close()

