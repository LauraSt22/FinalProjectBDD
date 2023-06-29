Feature: Access Terms and conditions page
  Background:
    Given sign_in: I want to read the terms and conditions

    @termsandconditions
    Scenario: Read the terms and conditions
      When sign_in: I click on terms and conditions
      When terms_and_conditions: I click the link for more information
      Then terms_and_conditions: I verify the url