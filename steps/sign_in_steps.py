from behave import *
# Given, Whenn, Aand, But, Then => Gherkin Syntax
# Gven seteaza situatia curenta
# When defineste pasii din test
# Then efectueaza verificarea testului


@Given('sign_in: I am a user on Jules app')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()

@When('sign_in: I set my email to "{email}"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)

@When('sign_in: I set my password to "{pwd}"')
def step_impl(context, pwd):
    context.sign_in_page.set_pwd(pwd)

@When('sign_in: I verify correct url')
def step_impl(context):
    context.sign_in_page.check_url_sign_in()

@When('sign_in: I click the login button')
def step_impl(context):
    context.sign_in_page.click_login_button()

@When('sign_in: I click the forgot password link')
def step_impl(context):
    context.sign_in_page.click_fogot_pwd_link()

@When('sign_in: I verify if message is displayed')
def step_impl(context):
    context.sign_in_page.verify_display_invalid_message()

@Then('sign_in: I am returned to the home page')
def step_impl(context):
    context.sign_in_page.check_current_url()




