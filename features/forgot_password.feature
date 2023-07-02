Feature: Jules forgot password tests
  # se ruleaza inainte de fiecare test
  Background:
    Given sign_in: I am a user on Jules app

    @passwordtesting
    Scenario:  Wrong email validation message
      When sign_in: I click the forgot password link
      When forgot_pass: I set my email to "abcd"
      Then forgot_pass: I verify that the email validation is correct


    @passwordtesting
    Scenario Outline: Wrong email validation message with table data
      When sign_in: I click the forgot password link
      When sign_in: I set my email to "<email_address>"
      Then forgot_pass: I verify that the email validation is correct

    Examples:
      | email_address   |
      | abcde.com |
      | test.com        |




