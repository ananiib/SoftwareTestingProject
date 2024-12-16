import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.homepage import Homepage
from pages.cartpage import CartPage
from behave import fixture


def get_driver():
    """Function to get and return the Chrome WebDriver"""
    chrome_install = ChromeDriverManager().install()
    service = ChromeService(executable_path=chrome_install)
    return webdriver.Chrome(service=service)


def before_all(context):
    """Initialize the WebDriver and store it in the context"""
    context.driver = get_driver()  # Get the WebDriver using the helper function
    context.driver.maximize_window()  # Optionally maximize the window


def after_all(context):
    """Clean up by quitting the WebDriver after all scenarios"""
    if hasattr(context, 'driver'):
        context.driver.quit()  # Quit the WebDriver after all scenarios


# Optional: Use this fixture if you need a separate instance for certain tests
@fixture
def browser(context):
    """Fixture for setting up a browser instance"""
    context.driver = get_driver()  # Initialize WebDriver
    yield context.driver  # Return the driver for the test
    context.driver.quit()  # Quit after the test


def before_scenario(context, scenario):
    """Initialize the WebDriver and open the homepage before each scenario"""
    context.driver = get_driver()  # Ensure we have the correct WebDriver setup
    context.homepage = Homepage(context.driver)  # Initialize the homepage
    context.homepage.open_page()  # Open the homepage


def after_scenario(context, scenario):
    """Quit the WebDriver after each scenario"""
    if hasattr(context, 'driver'):
        context.driver.quit()  # Quit the WebDriver after each scenario
