import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from pages.account_page import AccountPage
from pages.authorization_header import AuthorizationHeader
from pages.authorization_page import AuthorizationPage
from pages.order_page import OrderPage
from pages.registration_form import RegistrationForm
from pages.search_field import SearchField
from pages.search_page import SearchPage
from pages.shopping_cart import ShoppingCart


class TestSeleniumWebDriver(unittest.TestCase):

    def setUp(self) -> None:
        self.search_field = SearchField()
        self.search_page = SearchPage()
        self.authorization_header = AuthorizationHeader()
        self.authorization_page = AuthorizationPage()
        self.account_page = AccountPage()
        self.registration_form = RegistrationForm()
        self.shopping_cart = ShoppingCart()
        self.order_page = OrderPage()

        self.search_page.go_to_url(url='http://automationpractice.com/index.php')

    def tearDown(self) -> None:
        self.search_field.quit_driver()

    def test_search(self):
        # search field - OK
        self.search_field.search_item()

        # search field: elastic search - OK
        elastic_search = self.search_field.elastic_search_check()
        self.assertEqual(len(elastic_search), 5)

        # search field: search button - OK
        self.search_field.click_search_icon()

        # search page
        check_page_title = self.search_page.check_page_title()
        self.assertTrue(check_page_title)
        check_search_block = self.search_page.check_search_results_section()
        self.assertTrue(check_search_block)
        # time.sleep(5)
        nodes = self.search_page.results_found_number()
        self.assertEqual(len(nodes), 5)
        # time.sleep(20)

    def test_registration_success(self):
        # authorization header: click sign in button
        self.authorization_header.click_sign_in()

        # authorization page: fill email field
        self.authorization_page.register_email()

        # registration form: data fields and buttons
        self.registration_form.fill_registration_form()
        time.sleep(3)

        # account page:
        check_account_page_url = self.account_page.check_account_page()
        self.assertTrue(check_account_page_url)

        # authorization header: user name displayed and logout button
        header_name_display = self.authorization_header.check_user_name_account_page()
        self.assertTrue(header_name_display)
        # logging out
        self.authorization_header.logout()
        time.sleep(3)
        # asserting 'sign in' button is displayed again
        sign_in_button_displayed = self.authorization_header.check_sign_in_is_displayed()
        self.assertTrue(sign_in_button_displayed)

        # time.sleep(5)

    def test_add_to_cart(self):
        # search field: send keys & clicking search button
        self.search_field.search_item()
        self.search_field.click_search_icon()
        # time.sleep(5)
        # search page: change view icon and checking there are results
        nodes = self.search_page.results_found_number()
        self.assertTrue(len(nodes) > 0)
        # add to cart function: buttons, modal, shopping cart, shopping cart element
        cart_item = self.shopping_cart.add_to_cart()
        self.assertTrue(cart_item)
        time.sleep(3)
        # closing cart popup
        self.shopping_cart.close_cart_popup()
        time.sleep(3)
        # hover the cart
        self.shopping_cart.hover_on_cart()
        # self.shopping_cart.hover_2()

        # asserting there is a product in the cart
        self.assertTrue(self.shopping_cart.check_product_in_hover())
        time.sleep(3)
        self.shopping_cart.click_checkout_button()
        # check url of order page
        self.order_page.check_url()
        # check product quantity
        self.quantity = self.order_page.check_product_quantity()
        self.assertEqual(self.quantity, 1)


class TestTempHover(unittest.TestCase):

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(url="http://automationpractice.com/index.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.order_page = OrderPage()

    def test_add_to_cart_temp(self):
        # search field: send keys & button - OK
        self.driver.find_element(By.ID, "search_query_top").send_keys("Dress")
        self.driver.find_element(By.XPATH, "//button[@name='submit_search']").click()
        # time.sleep(5)
        # search page: change view icon - OK
        self.driver.find_element(By.CLASS_NAME, "icon-th-list").click()
        self.assertTrue(self.driver.find_element(By.ID, "center_column"))
        nodes = self.driver.find_elements(By.XPATH, "//ul[@class='product_list row list']/li")
        self.assertTrue(len(nodes) > 0)
        # add to cart function: buttons, modal, shopping cart, shopping cart element
        self.driver.find_element(By.XPATH, "//span[text()='Add to cart']").click()
        self.assertTrue(self.driver.find_element(By.ID, "layer_cart"))
        time.sleep(3)
        # closing cart popup
        self.driver.find_element(By.XPATH, "//*[@title='Continue shopping']/span").click()
        # hover the cart
        self.hover_cart = self.driver.find_element(By.XPATH, "//a[@title='View my shopping cart']")
        self.action = ActionChains(self.driver)
        self.action.move_to_element(self.hover_cart)
        time.sleep(3)
        self.action.perform()
        product_in_cart = self.driver.find_element(By.CSS_SELECTOR, ".products > .first_item")
        self.assertTrue(product_in_cart)
        self.driver.find_element(By.CSS_SELECTOR, "#button_order_cart").click()
        time.sleep(3)
        # order page
        # check url
        self.assertTrue(self.driver.current_url == "http://automationpractice.com/index.php?controller=order")
        # check product quantity
        self.quantity = self.driver.find_element(By.CSS_SELECTOR, ".cart_quantity_input").get_attribute("value")
        # self.quantity = self.order_page.check_product_quantity()
        self.assertEquals(int(self.quantity), 1)


if __name__ == '_main_':
    unittest.main()

