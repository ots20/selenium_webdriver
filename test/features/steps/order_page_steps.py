from behave import *
from hamcrest import equal_to, assert_that


@then("I get redirected to the order details page")
def step_impl(context):
    context.order_page.check_url()


@step("the item is displayed")
def step_impl(context):
    quantity = context.order_page.check_product_quantity()
    assert_that(quantity, equal_to(1))
