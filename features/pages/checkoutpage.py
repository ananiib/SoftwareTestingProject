from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ORDER_CONFIRMATION = (By.XPATH, "//h2[contains(text(), 'Thank you for your order')]")

    # Actions
    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Fill in the checkout form."""
        self.wait_for_element(self.FIRST_NAME_FIELD)
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)

        self.wait_for_element(self.LAST_NAME_FIELD)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)

        self.wait_for_element(self.POSTAL_CODE_FIELD)
        self.driver.find_element(*self.POSTAL_CODE_FIELD).send_keys(postal_code)

        return self

    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to be visible."""
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def submit_checkout(self):
        """
        Submit the checkout form by clicking the finish button.
        """
        # Wait until the finish button is clickable, then click it
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        self.driver.find_element(*self.FINISH_BUTTON).click()

