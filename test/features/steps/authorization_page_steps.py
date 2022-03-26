from behave import *


@step("I register my e-mail")
def step_impl(context):
    context.authorization_page.register_email()
