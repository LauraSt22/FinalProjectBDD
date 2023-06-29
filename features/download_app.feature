Feature: Jules download application for Google Play
  Background:
    Given download_app: I go to the sign in page

    @gettheapp
    Scenario: Get the App on Google Play
      When download_app: I want to download the app
      When download_app: I click on the install button
      Then download_app: I verify the message displayed


