from behave import *

@Given('sign_in: I want to read the terms and conditions')
def step_impl(context):
    context.terms_and_conditions.navigate_to_sign_in_page()

@When('sign_in: I click on terms and conditions')
def step_impl(context):
    context.terms_and_conditions.click_terms_conditions_button()

@When('terms_and_conditions: I click the link for more information')
def step_impl(context):
    context.terms_and_conditions.click_on_link()

@Then('terms_and_conditions: I verify the url')
def step_impl(context):
    context.terms_and_conditions.verify_url()