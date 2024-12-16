from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Socials:

    def __init__(self, context):
        self.context = context
        self.driver = self.context.driver  # WebDriver is assumed to be initialized in the context

    @given("the home page is opened in socials")
    def step_impl(context):
        context.driver.get("https://www.saucedemo.com/")
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )

    @given("the 'Username' field for socials is filled with '{username}'")
    def step_impl_fill_username_socials(context, username):
        username_field = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)

    @given("the 'Password' field for socials is filled with '{password}'")
    def step_impl_fill_password_socials(context, password):
        password_field = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(password)

    @given("the 'Login' button on homepage is clicked")
    def step_impl_click_login_homepage(context):
        login_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()

    @given("the 'Twitter' button for socials is clicked")
    def step_impl_click_twitter_button(context):
        button = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "social-twitter"))
        )
        button.click()

        WebDriverWait(context.driver, 5).until(lambda d: len(d.window_handles) > 1)
        context.driver.switch_to.window(context.driver.window_handles[-1])

    # Step: Click the 'Facebook' social media button
    @given("the 'Facebook' button for socials is clicked")
    def step_impl_click_facebook_button(context):
        button = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "social-facebook"))
        )
        button.click()

        WebDriverWait(context.driver, 5).until(lambda d: len(d.window_handles) > 1)
        context.driver.switch_to.window(context.driver.window_handles[-1])

    # Step: Click the 'LinkedIn' social media button
    @given("the 'LinkedIn' button for socials is clicked")
    def step_impl_click_linkedin_button(context):
        button = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "social-linkedIn"))
        )
        button.click()

        WebDriverWait(context.driver, 5).until(lambda d: len(d.window_handles) > 1)
        context.driver.switch_to.window(context.driver.window_handles[-1])

    '''@given("the '{social_media}' for socials button is clicked")
    def step_impl_click_social_button(context, social_media):
        button_mapping = {
            "Twitter": "social-twitter",
            "Facebook": "social-facebook",
            "LinkedIn": "social-linkedIn",
        }
        button_id = button_mapping[social_media]
        button = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, button_id))
        )
        button.click()

        WebDriverWait(context.driver, 5).until(lambda d: len(d.window_handles) > 1)
        context.driver.switch_to.window(context.driver.window_handles[-1])'''

    @then("the user is redirected to 'https://x.com/saucelabs'")
    def step_impl_verify_redirection_x(context):
        # Wait for the URL to contain the specific expected URL
        WebDriverWait(context.driver, 15).until(
            EC.url_contains("https://x.com/saucelabs")
        )

        current_url = context.driver.current_url
        print(f"Current URL after redirection: {current_url}")

        # Assert that the current URL matches the expected one
        assert current_url == "https://x.com/saucelabs", \
            f"Expected to be redirected to 'https://x.com/saucelabs', but got {current_url}"

    @then("the user is redirected to 'https://www.facebook.com/saucelabs'")
    def step_impl_verify_redirection_facebook(context):
        # Wait for the URL to contain the specific expected URL
        WebDriverWait(context.driver, 15).until(
            EC.url_contains("https://www.facebook.com/saucelabs")
        )

        current_url = context.driver.current_url
        print(f"Current URL after redirection: {current_url}")

        # Assert that the current URL matches the expected one
        assert current_url == "https://www.facebook.com/saucelabs", \
            f"Expected to be redirected to 'https://www.facebook.com/saucelabs', but got {current_url}"

    @then("the user is redirected to 'https://www.linkedin.com/company/sauce-labs/'")
    def step_impl_verify_redirection_linkedin(context):
        # Wait for the URL to contain the specific expected URL
        WebDriverWait(context.driver, 15).until(
            EC.url_contains("https://www.linkedin.com/company/sauce-labs/")
        )

        current_url = context.driver.current_url
        print(f"Current URL after redirection: {current_url}")

        # Assert that the current URL matches the expected one
        assert current_url == "https://www.linkedin.com/company/sauce-labs/", \
            f"Expected to be redirected to 'https://www.linkedin.com/company/sauce-labs/', but got {current_url}"

