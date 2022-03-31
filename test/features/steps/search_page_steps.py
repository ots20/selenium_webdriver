from behave import *
from hamcrest import assert_that, is_, greater_than


@then("the search results page is displayed")
def step_impl(context):
    check_search_block = context.search_page.check_search_results_section()
    assert_that(check_search_block)


@step("five items are displayed")
def step_impl(context):
    nodes = context.search_page.results_found_number()
    assert_that(len(nodes), is_(5))


@then("the search page displays the results")
def step_impl(context):
    nodes = context.search_page.results_found_number()
    assert_that(len(nodes), greater_than(0))
