import unittest
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
        # When I type "printed dress" in the search field
        self.search_field.search_item()
        # Then five results are displayed under the search field
        elastic_search = self.search_field.elastic_search_check()
        self.assertEqual(len(elastic_search), 5)
        # When I click the search icon
        self.search_field.click_search_icon()
        # Then the search results page is displayed
        check_search_block = self.search_page.check_search_results_section()
        self.assertTrue(check_search_block)
        # And five items are displayed
        nodes = self.search_page.results_found_number()
        self.assertEqual(len(nodes), 5)

    def test_registration_success(self):
        print("TC - registration")
        # When I click the sign-in button
        self.authorization_header.click_sign_in()
        # And I register my e-mail
        self.authorization_page.register_email()
        # Then the registration form is presented
        reg_form_displayed = self.registration_form.check_reg_form_display()
        self.assertTrue(reg_form_displayed)
        # When I fill the registration form successfully
        self.registration_form.fill_registration_form()
        # Then I get log in with my name displayed in the header
        header_name_display = self.authorization_header.check_user_name_account_page()
        self.assertTrue(header_name_display)

        # When I click the logout button
        self.authorization_header.logout()
        # Then the sign-in button is displayed again in the header
        sign_in_button_displayed = self.authorization_header.check_sign_in_is_displayed()
        self.assertTrue(sign_in_button_displayed)

    def test_add_to_cart(self):
        print("TC - add to cart")
        # search field: send keys & clicking search button
        # When I search an item
        self.search_field.search_item()
        self.search_field.click_search_icon()
        # search page: change view icon and checking there are results
        # Then the search page displays the results
        nodes = self.search_page.results_found_number()
        self.assertTrue(len(nodes) > 0)
        # add to cart function: buttons, modal, shopping cart, shopping cart element
        # When I add an item to the cart
        cart_item = self.shopping_cart.add_to_cart()
        self.assertTrue(cart_item)
        # closing cart popup
        # And I close the modal popup
        self.shopping_cart.close_cart_popup()
        # hover the cart
        # And I hover the cart
        self.shopping_cart.check_popup_closed()
        self.shopping_cart.hover_on_cart()
        # asserting there is a product in the cart
        # Then the item is displayed in the cart
        self.assertTrue(self.shopping_cart.check_product_in_hover())
        # When I click the checkout button
        self.shopping_cart.click_checkout_button()
        # check url of order page
        # Then I get redirected to the order details page
        self.order_page.check_url()
        # check product quantity
        # And the item is displayed
        self.quantity = self.order_page.check_product_quantity()
        self.assertEqual(self.quantity, 1)

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearing down")
        cls.search_page.quit_driver()


if __name__ == '_main_':
    unittest.main()

