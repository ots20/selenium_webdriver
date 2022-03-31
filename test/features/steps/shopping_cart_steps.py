from behave import *
from hamcrest import assert_that


@when("I add an item to the cart")
def step_impl(context):
    cart_item = context.shopping_cart.add_to_cart()
    assert_that(cart_item)


@step("I close the modal popup")
def step_impl(context):
    context.shopping_cart.close_cart_popup()


@step("I hover the cart")
def step_impl(context):
    context.shopping_cart.check_popup_closed()
    context.shopping_cart.hover_on_cart()


@then("the item is displayed in the cart")
def step_impl(context):
    assert_that(context.shopping_cart.check_product_in_hover())


@when("I click the checkout button")
def step_impl(context):
    context.shopping_cart.click_checkout_button()


