Feature: Jules download application for Apple
  Background:
    Given download_app_for_apple: I go to the sign in page

    @gettheappleapp
    Scenario: Get the App on Apple Store
      When download_app_for_apple: I want to get the apple app and I click on the download app store button
      Then download_app_for_apple: I am redirected to a page where I have instructions to download the app