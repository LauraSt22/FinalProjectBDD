from behave import *

@When('forgot_pass: I set my email to "{email}"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)

@Then('forgot_pass: I verify that the email validation is correct')
def step_impl(context):
    context.forgot_pass.verify_error_email_message()



