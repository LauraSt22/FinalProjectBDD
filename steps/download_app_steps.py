from behave import *


@Given('download_app: I go to the sign in page')
def step_impl(context):
    context.download_app.navigate_to_sign_in_page()

@When('download_app: I want to download the app')
def step_impl(context):
    context.download_app.click_download_for_google()

@When('download_app: I click on the install button')
def step_impl(context):
    context.download_app.click_install_button()

@Then('download_app: I verify the message displayed')
def step_impl(context):
    context.download_app.check_diplay_message_if_not_connected()
