Feature: User Login

  Background:
    Given the home page is opened

  Scenario Outline: Incorrect login attempts
    Given the 'Username' field is filled with '<username>'
    And the 'Password' field is filled with '<password>'
    When the 'Login' button is clicked
    Then the '<errorMessage>' message is shown
    Examples:
      | username        | password       | errorMessage                                                              |
      | ""              | ""             | Epic sadface: Username and password do not match any user in this service |
      | standard_user   | ""             | Epic sadface: Username and password do not match any user in this service |
      | standard_user   | wrong_password | Epic sadface: Username and password do not match any user in this service |
      | locked_out_user | secret_sauce   | Epic sadface: Sorry, this user has been locked out.                       |

  Scenario Outline: Successful login
    Given the 'Username' field is filled with '<username>'
    And the 'Password' field is filled with '<password>'
    When the 'Login' button is clicked
    Then the home page should be displayed
    Examples:
      | username                       | password     |
      | standard_user                  | secret_sauce |
      | visual_user                    | secret_sauce |
      | problem_user                   | secret_sauce   |
      | performance_glitch_user        | secret_sauce   |
      |  error_user                    | secret_sauce   |

  Scenario Outline: Login with special characters
    Given the 'Username' field is filled with '<username>'
    And the 'Password' field is filled with '<password>'
    When the 'Login' button is clicked
    Then the '<errorMessage>' message is shown
    Examples:
      | username   | password     | errorMessage                                                              |
      | '!@#$%'    | 'password123'| Epic sadface: Username and password do not match any user in this service |
      | 'user'     | '!@#123'     | Epic sadface: Username and password do not match any user in this service |


  Scenario Outline: Handling different types of inputs
    Given the home page is opened
    And the 'Username' field is filled with '<username>'
    And the 'Password' field is filled with '<password>'
    When the 'Login' button is clicked
    Then the '<error_message>' message is shown
    Examples:
      | username   | password     | error_message                                                           |
      | '!@#$%'    | 'password123'| Epic sadface: Username and password do not match any user in this service |
      | 'user'     | '!@#123'     | Epic sadface: Username and password do not match any user in this service |
      | 'verylongusername' | 'verylongpassword' | Epic sadface: Username and password do not match any user in this service |

  Scenario: User navigates to the cart after logging in
    Given the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    When the 'Login' button is clicked
    Then the home page should be displayed
    When the user navigates to the cart
    Then the cart page should be displayed
