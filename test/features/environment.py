from pages.account_page import AccountPage
from pages.authorization_header import AuthorizationHeader
from pages.authorization_page import AuthorizationPage
from pages.order_page import OrderPage
from pages.registration_form import RegistrationForm
from pages.search_field import SearchField
from pages.search_page import SearchPage
from pages.shopping_cart import ShoppingCart
from utils.capabilities_util import get_driver


def before_all(context):
    # Setting up global variables
    setup = context.config.userdata
    context.driver = get_driver(browser=setup["browser"])
    # Setting up page objects
    context.search_field = SearchField(context=context)
    context.search_page = SearchPage(context=context)
    context.authorization_header = AuthorizationHeader(context=context)
    context.authorization_page = AuthorizationPage(context=context)
    context.account_page = AccountPage(context=context)
    context.registration_form = RegistrationForm(context=context)
    context.shopping_cart = ShoppingCart(context=context)
    context.order_page = OrderPage(context=context)
    # Opening the page
    context.search_page.go_to_url(url='http://automationpractice.com/index.php')


def after_all(context):
    context.search_page.quit_driver()
