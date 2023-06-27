from behave import *

@Given('sign_up: I want to sign up')
def step_impl(context):
    context.sign_up_page.navigate_to_sign_up_page()


@When('sign_up: I click the sign up button')
def step_impl(context):
    context.sign_up_page.click_sign_up_button()

@When('sign_up: I click on the selection of the personal')
def step_impl(context):
    context.sign_up_page.select_option()

@When('sign_up: I click the continue button')
def step_impl(context):
    context.sign_up_page.click_continue_button()

@When('sign_up: I set my first name to first_name')
def step_impl(context, first_name):
    context.sign_up_page.add_first_name(first_name)

@When('sign_up: I set my last name to {last_name}')
def step_impl(context, last_name):
    context.sign_up_page.add_last_name(last_name)

@When('sign_up: I set my email to {email}')
def step_impl(context, email):
    context.sign_up_page.add_email(email)

@When('sign_up: I set correct email to {correct_email}')
def step_impl(context, correct_email):
    context.sign_up_page.add_correct_email(correct_email)

@When('sign_in: I verify if I am on the correct page')
def step_impl(context):
    context.sign_up_page.check_url_sign_up()

@When('sign_up: I verify correct url')
def step_impl(context):
    context.sign_up_page.check_url_sign_up()

@Then('sign_up: I verify if message wrong email is displayed')
def step_impl(context):
    context.sign_up_page.verify_display_invalid_email()

@Then('sign_up: I verify if the wrong email message is displayed after entered correct email')
def step_impl(context):
    context.sign_up_page.verify_display_invalid_email()
