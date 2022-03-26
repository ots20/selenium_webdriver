from time import sleep

from behave import *
from hamcrest import assert_that, is_


@when('I type "printed dress" in the search field')
def step_impl(context):
    context.search_field.search_item()


@then("five results are displayed under the search field")
def step_impl(context):
    elastic_search = context.search_field.elastic_search_check()
    # context.assertEqual(len(elastic_search), 5)
    assert_that(len(elastic_search), is_(5))


@when("I click the search icon")
def step_impl(context):
    context.search_field.click_search_icon()


@when("I search an item")
def step_impl(context):
    context.search_field.search_item()
    context.search_field.click_search_icon()
