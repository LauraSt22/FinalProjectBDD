Feature: Jules sign up tests

  Background:
    Given sign_up: I want to sign up

    @sign_up
    Scenario Outline: Successful validation message
      When sign_up: I click the sign up button
      When sign_up: I click on the selection of the personal
      When sign_up: I click the continue button
      When sign_up: I entered my "<first name>"
      When sign_up: I entered my "<last name>"
      When sign_up: I entered the correct "<email>"
      When sign_in: I verify if message wrong email is displayed after entered correct email


    Examples:
      | first_name   |    | last_name  |  | email_address          |
      | First        |    | Last       |  | first_last@email.com   |
      | Laura        |    | Stanciu    |  | mail@email.com         |
      | Test         |    | Signin     |  | test@email.com         |