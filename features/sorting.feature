Feature: Sort items

  Background:
    Given the home page is opened

    Scenario: Sort items by name (A-Z)
      Given the 'Username' field is filled with 'standard_user'
      And the 'Password' field is filled with 'secret_sauce'
      And the 'Login' button is clicked
      When the user selects "Name (A to Z)" from the sorting options
      Then the items should be sorted in ascending order by name

    Scenario: Sort items by name
      Given the 'Username' field is filled with 'standard_user'
      And the 'Password' field is filled with 'secret_sauce'
      And the 'Login' button is clicked
      When the user selects "Name (Z to A)" from the sorting options
      Then the items should be sorted in descending order by name

    Scenario Outline: Sorting by Price (low to high, high to low)
      Given the user is logged in to Saucedemo
      When the user clicks on the "menu" button
      And the user selects the "Products" option
      And the user selects the "<sort_option>" sorting option
      Then the products should be sorted by price in the "<sort_order>" order

      Examples:
        | sort_option               | sort_order   |
        | Price (low to high)       | ascending    |
        | Price (high to low)       | descending   |
