# Python Behave Example Project

This project demonstrates how to use **Python Behave**, a Behavior-Driven Development (BDD) framework, to write and execute functional tests. The tests are designed to interact with the **Saucedemo** website, a sample e-commerce platform, to validate key functionalities such as login, navigation, and product interactions.

## Project Structure📃

```
project-root/
|-- features/
|   |-- pages/
|   |-- steps/
|   |   |-- step_definitions.py  # Step implementations for Behave scenarios
|   |-- login.feature            # Feature files defining test scenarios
|-- environment.py               # Hooks for setup and teardown
|-- requirements.txt             # Python dependencies
|-- README.md                    # Project documentation (this file)
```

## Prerequisites🎟️

Before running the project, ensure you have the following installed:

1. **Python 3.8+**
2. **pip** (Python package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Tests

To execute the tests, use the following command:

```bash
behave
```

This will run all feature files in the `features/` directory.

### Specifying Features or Scenarios

To run a specific feature or scenario, provide the path to the `.feature` file:

```bash
behave features/login.feature
```

You can also target a specific scenario by using tags:

```bash
behave --tags=@login
```

## Key Components

### `features/`

This folder contains:

- **Feature files**: Define scenarios in plain English (Gherkin syntax).
- **Step definitions**: Implement the steps defined in the feature files using Python.

### `environment.py`

Manages the test environment setup and teardown, such as initializing and closing browser instances.

## Testing Against Saucedemo

The project uses [Saucedemo](https://www.saucedemo.com/) as the application under test. Ensure you have access to the site for successful test execution.

### Example Scenario

The `login.feature` file includes scenarios like:

```gherkin
Feature: Logout functionality on Saucedemo

  Scenario: User logs out of Saucedemo successfully
    Given the user is logged in to Saucedemo
    When the user clicks on the "menu" button
    And the user selects the "Logout" option
    Then the user should be redirected to the login page
    And the login page should display the login form

```

### Step Definitions Example

Steps for the above scenario are implemented in `step_definitions.py`:

```python
from behave import given, when, then
from selenium import webdriver

@given('the user is logged in to Saucedemo')
def step_impl_given_logged_in(context):
    context.driver = webdriver.Chrome()  # or use any other browser you prefer
    context.driver.get("https://www.saucedemo.com")

    # Perform login with credentials
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()
    sleep(2)  # Wait for the page to load


@when('the user clicks on the "menu" button')
def step_impl_click_menu(context):
    menu_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
    menu_button.click()

    # Wait for the menu to fully expand
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
    )
```

## Enhancements

- Add additional feature files for more functionality (e.g., adding items to the cart, checking out).
- Integrate with CI/CD pipelines to run tests automatically.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

