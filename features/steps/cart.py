from hamcrest import assert_that, equal_to
from features.pages.cartpage import CartPage
from behave import when, step


@when("the user navigates to the cart")
def step_impl(context):
    context.cart = CartPage(context.driver)
    context.cart.open_page()


@step("the cart page should be displayed")
def step_impl(context):
    assert_that(context.cart.is_cart_page_displayed(), equal_to(True))
