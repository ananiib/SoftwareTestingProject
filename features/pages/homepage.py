from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage:
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to cart']")
    text_fields = {
        "Username": (By.ID, "user-name"),
        "Password": (By.ID, "password")
    }

    navigation_buttons = {
        "Login": (By.ID, "login-button"),
        "Twitter": (By.ID, "social-twitter"),
        "Facebook": (By.ID, "social-facebook"),
        "LinkedIn": (By.ID, "social-linkedIn"),
    }

    messages = {
        "Login Error": (
            By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")
    }

    checkout_fields = {
        "Username": (By.ID, "user-name"),
        "Password": (By.ID, "password"),
        "First Name": (By.ID, "first-name"),
        "Last Name": (By.ID, "last-name"),
        "Postal Code": (By.ID, "postal-code")
    }

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")
        self.wait_for_element(self.text_fields["Username"])

    def close_page(self):
        self.driver.quit()

    def fill_out_field(self, field, text):
        self.driver.find_element(*self.text_fields[field]).send_keys(text)

    def click_button(self, button):
        if button not in self.navigation_buttons:
            raise ValueError(f"Button '{button}' not found in navigation buttons.")
        self.driver.find_element(*self.navigation_buttons[button]).click()

    def get_error_message(self):
        return self.driver.find_element(*self.messages["Login Error"]).text

    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to be present and visible."""
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def add_product_to_cart(self, product_name):
        """Add a product to the cart by its name"""
        # Assuming product_name is unique and can be used to locate the add-to-cart button
        product_locator = f"//div[text()='{product_name}']/following-sibling::button"
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, product_locator))
        )
        add_button.click()

    def fill_checkout_field(self, field, value):
        """Fill out a specific checkout field with the provided value."""
        try:
            element = self.driver.find_element(*self.checkout_fields[field])
            element.clear()  # Clear any existing text
            element.send_keys(value)  # Fill the field with the provided value
        except KeyError:
            raise ValueError(f"Field '{field}' not found in checkout_fields")
        except Exception as e:
            raise RuntimeError(f"Failed to fill the field '{field}'. Error: {e}")
