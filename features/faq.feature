Feature: FAQ page
  Background:
    Given sign_in: I want to read the FAQ

    @gettheapp
    Scenario: Read the FAQ
      When sign_in: I click on FAQ
      Then faq: I verify if the text is therefaq: I verify if the text is there