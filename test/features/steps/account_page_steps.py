from behave import *
from hamcrest import assert_that


@then("I get logged in with my name displayed in the header")
def step_impl(context):
    header_name_display = context.authorization_header.check_user_name_account_page()
    assert_that(header_name_display)