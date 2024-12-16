from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize the driver (can be done in a before hook if you prefer)
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


@when('the user selects the "Logout" option')
def step_impl_select_logout(context):
    context.driver.find_element(By.ID, "logout_sidebar_link").click()
    sleep(2)  # Wait for logout to complete


@then('the user should be redirected to the login page')
def step_impl_redirect_to_login(context):
    assert context.driver.current_url == "https://www.saucedemo.com/"


@then('the login page should display the login form')
def step_impl_see_login_form(context):
    # Ensure the login form is visible by checking the presence of username and password fields
    assert context.driver.find_element(By.ID, "user-name").is_displayed()
    assert context.driver.find_element(By.ID, "password").is_displayed()

    # Optionally close the driver after the test
    context.driver.quit()
