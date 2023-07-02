from behave import *

@Given('sign_in: I want to read the FAQ')
def step_impl(context):
    context.faq.navigate_to_sign_in_page()

@When('sign_in: I click on FAQ')
def step_impl(context):
    context.faq.click_on_faq()

@Then('faq: I verify if the text is there')
def step_impl(context):
    context.faq.check_page_is_not_empty()