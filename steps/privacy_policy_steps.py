from behave import *

@Given('sign_in: I want to read the privacy policy')
def step_impl(context):
    context.privacy_policy.navigate_to_sign_in_page()

@When('sign_in: I click on privacy policy')
def step_impl(context):
    context.privacy_policy.click_on_privacy()

@Then('privacy_policy: I verify if the text is there')
def step_impl(context):
    context.privacy_policy.check_wrinting()