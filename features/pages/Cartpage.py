from selenium.webdriver.common.by import By
from .checkoutpage import CheckoutPage


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def is_cart_page_displayed(self):
        return self.driver.find_element(By.CLASS_NAME, "cart_list").is_displayed()

    def get_cart_products(self):
        """Retrieve the list of products in the cart"""
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")  # Example locator
        return [product.text for product in products]

    def proceed_to_checkout(self):
        """Click on the checkout button to navigate to the checkout form"""
        checkout_button = self.driver.find_element(By.ID, "checkout")  # Use By.ID
        checkout_button.click()

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        return CheckoutPage(self.driver)

    def add_product_to_cart(self, product_name):
        product = self.driver.find_element(By.XPATH, f"//div[@class='product_name' and text()='{product_name}']")
