Feature: Valid Social Media

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login' button is clicked

  Scenario: Verify the twitter button
    Given the 'Twitter' button is clicked
    Then the user is redirected to 'https://x.com/saucelabs'

  Scenario: Verify the facebook button
    Given the 'Facebook' button is clicked
    Then the user is redirected to 'https://www.facebook.com/saucelabs'

  Scenario: Verify the linkedin button
    Given the 'LinkedIn' button is clicked
    Then the user is redirected to 'https://www.linkedin.com/company/sauce-labs/'
