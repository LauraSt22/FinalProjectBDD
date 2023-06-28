Feature: Jules sign up tests

  Background:
    Given sign_up: I want to sign up

    @sign_up
    Scenario: Successful validation message
      When sign_up: I click the sign up button
      When sign_up: I click on the selection of the personal
      When sign_up: I click the continue button
      When sign_up: I set my first name to "<first name>"
      When sign_up: I set my last name to "<last name>"
      When sign_up: I set my email to "first_last"
      Then sign_in: I verify if message "Please enter a valid email address." is displayed in the application
