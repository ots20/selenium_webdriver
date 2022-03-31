from behave import *
from hamcrest import assert_that


@then("the registration form is presented")
def step_impl(context):
    reg_form_displayed = context.registration_form.check_reg_form_display()
    assert_that(reg_form_displayed)


@when("I fill the registration form successfully")
def step_impl(context):
    context.registration_form.fill_registration_form()
