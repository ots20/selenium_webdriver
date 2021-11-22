import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage
from pages.account_page import AccountPage
from pages.authorization_header import AuthorizationHeader
from pages.authorization_page import AuthorizationPage
from pages.order_page import OrderPage
from pages.registration_form import RegistrationForm
from pages.search_field import SearchField
from pages.search_page import SearchPage
from pages.shopping_cart import ShoppingCart


class TestSeleniumWebDriver(unittest.TestCase, BasePage):

    # def setUp(self) -> None:
    #     print("setting up")
    #     self.search_field = SearchField()
    #     self.search_page = SearchPage()
    #     self.authorization_header = AuthorizationHeader()
    #     self.authorization_page = AuthorizationPage()
    #     self.account_page = AccountPage()
    #     self.registration_form = RegistrationForm()
    #     self.shopping_cart = ShoppingCart()
    #     self.order_page = OrderPage()
    #     self.go_to_url(url='http://automationpractice.com/index.php')

    @classmethod
    def setUpClass(cls) -> None:
        print("starting")
        cls.search_field = SearchField()
        cls.search_page = SearchPage()
        cls.authorization_header = AuthorizationHeader()
        cls.authorization_page = AuthorizationPage()
        cls.account_page = AccountPage()
        cls.registration_form = RegistrationForm()
        cls.shopping_cart = ShoppingCart()
        cls.order_page = OrderPage()
        cls.search_page.go_to_url(url='http://automationpractice.com/index.php')

    def test_search(self):
        print("TC - test_search")
        # search field - OK
        self.search_field.search_item()

        # search field: elastic search - OK
        elastic_search = self.search_field.elastic_search_check()
        self.assertEqual(len(elastic_search), 5)

        # search field: search button - OK
        self.search_field.click_search_icon()

        # search page
        # check_page_title = self.search_page.check_page_title()
        # self.assertTrue(check_page_title)
        check_search_block = self.search_page.check_search_results_section()
        self.assertTrue(check_search_block)
        nodes = self.search_page.results_found_number()
        self.assertEqual(len(nodes), 5)

    def test_registration_success(self):
        print("TC - registration")
        # authorization header: click sign in button
        self.authorization_header.click_sign_in()

        # authorization page: fill email field
        self.authorization_page.register_email()

        # registration form: data fields and buttons
        self.registration_form.fill_registration_form()

        # account page:
        # check_account_page_url = self.account_page.check_account_page()
        # self.assertTrue(check_account_page_url)

        # authorization header: user name displayed and logout button
        header_name_display = self.authorization_header.check_user_name_account_page()
        self.assertTrue(header_name_display)
        # logging out
        self.authorization_header.logout()
        # asserting 'sign in' button is displayed again
        sign_in_button_displayed = self.authorization_header.check_sign_in_is_displayed()
        self.assertTrue(sign_in_button_displayed)

    def test_add_to_cart(self):
        print("TC - add to cart")
        # search field: send keys & clicking search button
        self.search_field.search_item()
        self.search_field.click_search_icon()
        # search page: change view icon and checking there are results
        nodes = self.search_page.results_found_number()
        self.assertTrue(len(nodes) > 0)
        # add to cart function: buttons, modal, shopping cart, shopping cart element
        cart_item = self.shopping_cart.add_to_cart()
        self.assertTrue(cart_item)
        # closing cart popup
        self.shopping_cart.close_cart_popup()
        # hover the cart
        self.shopping_cart.check_popup_closed()
        self.shopping_cart.hover_on_cart()
        # asserting there is a product in the cart
        self.assertTrue(self.shopping_cart.check_product_in_hover())
        self.shopping_cart.click_checkout_button()
        # check url of order page
        self.order_page.check_url()
        # check product quantity
        self.quantity = self.order_page.check_product_quantity()
        self.assertEqual(self.quantity, 1)

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearing down")
        cls.search_page.quit_driver()


if __name__ == '_main_':
    unittest.main()

