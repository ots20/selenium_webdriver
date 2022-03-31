from behave import *
from hamcrest import assert_that


@when("I click the sign-in button")
def step_impl(context):
    context.authorization_header.click_sign_in()


@when("I click the logout button")
def step_impl(context):
    context.authorization_header.logout()


@then("the sign-in button is displayed again in the header")
def step_impl(context):
    sign_in_button_displayed = context.authorization_header.check_sign_in_is_displayed()
    assert_that(sign_in_button_displayed)