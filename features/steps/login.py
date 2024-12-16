from behave import *
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By
from features.pages.homepage import Homepage


@step("the home page is opened")
def step_impl(context):
    context.homepage.open_page()


@step("the '{field}' field is filled with '{text}'")
def step_fill_field(context, field, text):
    field = '' if field == '[blank]' else field
    text = '' if text == '[blank]' else text
    context.homepage.fill_out_field(field, text)


@step("the '{button}' button is clicked")
def step_impl_click_button(context, button):
    try:
        context.homepage.click_button(button)
    except Exception as e:
        print(f"Error clicking button '{button}': {e}")
        raise


@given("the 'Twitter' button is clicked")
def step_impl_click_twitter(context):
    context.homepage.click_button("Twitter")


@given("the 'Facebook' button is clicked")
def step_impl_click_facebook(context):
    context.homepage.click_button("Facebook")  # Matches the key in navigation_buttons


@given("the 'LinkedIn' button is clicked")
def step_impl_click_linkedin(context):
    context.homepage.click_button("LinkedIn")  # Matches the key in navigation_buttons


@step("the '{error}' message is shown")
def step_impl(context, error):
    assert_that(context.homepage.get_error_message(), equal_to(error))


@step("the home page should be displayed")
def step_impl(context):
    homepage_element = context.homepage.driver.find_element(By.CLASS_NAME, "inventory_list")
    assert_that(homepage_element.is_displayed(), equal_to(True))


@when('the "{field}" field with "{value}"')
def step_impl(context, field, value):
    print(f"Filling field: {field}, value: {value}")
    context.homepage.fill_checkout_field(field, value)


@when(u'the user opens the homepage')
def step_impl(context):
    # Ensure homepage is initialized
    print(f"Homepage: {context.homepage}")  # This will show if context.homepage is None or an actual object
    context.homepage.open_page()


@given('the user is on the homepage')
def step_impl(context):
    context.homepage = Homepage(context.driver)


@given('the user is logged in as a valid user')
def step_impl(context):
    context.login_page.login("standard_user", "secret_sauce")
