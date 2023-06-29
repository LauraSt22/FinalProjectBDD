Feature: Privacy Policy page
  Background:
    Given sign_in: I want to read the privacy policy

    @gettheapp
    Scenario: Read the Privacy Policy
      When sign_in: I click on privacy policy
      Then privacy_policy: I verify if the text is there