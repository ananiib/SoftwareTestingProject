from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@given("the 'Username' field is filled with '{username}'")
def step_impl_fill_username_sorting(context, username):
    username_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username_field.send_keys(username)


@given("the 'Password' field is filled with '{password}'")
def step_impl_fill_password_sorting(context, password):
    password_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_field.send_keys(password)


@given("the 'Login' button is clicked")
def step_impl_click_login_sorting(context):
    login_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()


@when('the user selects the "Products" option')
def step_impl_select_products(context):
    products_link = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "inventory_sidebar_link"))
    )
    products_link.click()

    # Wait for the product page to load
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )


@when('the user selects the "{sort_option}" sorting option')
def step_impl_select_sort_option(context, sort_option):
    sort_dropdown = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )
    select = Select(sort_dropdown)
    select.select_by_visible_text(sort_option)

    # Wait for products to reload after sorting
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )


@then('the products should be sorted by price in the "{sort_order}" order')
def step_impl_verify_sorted_price(context, sort_order):
    product_prices = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price"))
    )
    price_list = [float(price.text.strip('$')) for price in product_prices]

    if sort_order == "ascending":
        assert price_list == sorted(price_list), f"Expected ascending order, but got {price_list}"
    elif sort_order == "descending":
        assert price_list == sorted(price_list, reverse=True), f"Expected descending order, but got {price_list}"


@when('the user selects "Name (Z to A)" from the sorting options')
def step_impl(context):
    # Locate the dropdown element for sorting using the correct driver reference
    sort_dropdown = context.driver.find_element(By.CLASS_NAME, "product_sort_container")

    # Create a Select object to interact with the dropdown
    select = Select(sort_dropdown)

    # Select the "Name (Z to A)" option
    select.select_by_visible_text("Name (Z to A)")


@when('the user selects "Name (A to Z)" from the sorting options')
def step_impl(context):
    # Wait for the sorting dropdown to be visible
    sort_dropdown = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )

    # Click the dropdown
    sort_dropdown.click()

    # Wait for the "Name (A to Z)" option to be visible and then click it
    name_option = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//option[text()='Name (A to Z)']"))
    )

    name_option.click()


@then("the items should be sorted in ascending order by name")
def step_impl(context):
    # Fetch the list of product names displayed on the webpage
    product_names = context.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
    product_names_text = [item.text for item in product_names]

    # Check if the list is sorted in ascending order
    assert product_names_text == sorted(product_names_text), \
        f"Products are not sorted in ascending order by name: {product_names_text}"


@then("the items should be sorted in descending order by name")
def step_impl(context):
    # Retrieve the list of items from the page
    items = context.driver.find_elements(By.CLASS_NAME, "inventory_item_name")  # Update the selector based on your HTML

    # Extract the names of the items
    item_names = [item.text for item in items]

    # Verify the items are sorted in descending order
    sorted_names = sorted(item_names, reverse=True)  # Descending order
    assert item_names == sorted_names, f"Items are not sorted in descending order by name. Actual order: {item_names}"


@given("the home page is opened")
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
