Feature: Logout functionality on Saucedemo

  Scenario: User logs out of Saucedemo successfully
    Given the user is logged in to Saucedemo
    When the user clicks on the "menu" button
    And the user selects the "Logout" option
    Then the user should be redirected to the login page
    And the login page should display the login form
