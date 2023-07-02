Feature: Jules sign in tests

  Background:
    Given sign_in: I am a user on Jules app

    @logare
    Scenario: Verify user can login with valid username and password
      When sign_in: I set my email to "email_address"
      When sign_in: I set my password to "password"
      When sign_in: I click the login button
      Then sign_in: The user is redirected to the julesapp homepage "https://jules.app/search/all"
