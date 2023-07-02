from behave import *

@Given('download_app_for_apple: I go to the sign in page')
def step_impl(context):
    context.download_app_for_apple.navigate_to_sign_in_page()

@When('download_app_for_apple: I want to get the apple app and I click on the download app store button')
def step_impl(context):
    context.download_app_for_apple.click_download_for_apple()

@Then('download_app_for_apple: I am redirected to a page where I have instructions to download the app')
def step_impl(context):
    context.download_app_for_apple.message_displayed_to_get_the_app()