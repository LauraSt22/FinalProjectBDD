Feature: Jules sign in tests

  Background:
    Given sign_in: I am a user on Jules app

    @logare
    Scenario Outline: Verify button is disabled
      When sign_in: I verify correct url
      When sign_in: I set my email to "<email_address>"
      Then sign_in: I am returned to the home page

    Examples:
      | first_name   |    | last_name  |  | email_address          |
      | First        |    | Last       |  | first_last@email.com   |
      | Laura        |    | Stanciu    |  | mail@email.com         |
      | Test         |    | Signin     |  | test@email.com         |