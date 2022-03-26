from pages.account_page import AccountPage
from pages.authorization_header import AuthorizationHeader
from pages.authorization_page import AuthorizationPage
from pages.order_page import OrderPage
from pages.registration_form import RegistrationForm
from pages.search_field import SearchField
from pages.search_page import SearchPage
from pages.shopping_cart import ShoppingCart


def before_all(context):
    context.search_field = SearchField()
    context.search_page = SearchPage()
    context.authorization_header = AuthorizationHeader()
    context.authorization_page = AuthorizationPage()
    context.account_page = AccountPage()
    context.registration_form = RegistrationForm()
    context.shopping_cart = ShoppingCart()
    context.order_page = OrderPage()
    context.search_page.go_to_url(url='http://automationpractice.com/index.php')


def after_all(context):
    context.search_page.quit_driver()