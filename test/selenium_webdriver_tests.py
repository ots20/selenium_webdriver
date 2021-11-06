import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class TestSeleniumWebDriver(unittest.TestCase):

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(url="http://automationpractice.com/index.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_search(self):
        # search field
        self.driver.find_element(By.ID, "search_query_top").send_keys("Printed dress")
        # time.sleep(6)
        # search field: elastic search
        elastic_search = self.driver.find_elements(By.CSS_SELECTOR, ".ac_results > ul > li")
        self.assertEqual(len(elastic_search), 5)
        # search field: search button
        self.driver.find_element(By.XPATH, "//button[@name='submit_search']").click()
        # search page
        self.assertTrue(self.driver.title == 'Search - My Store')
        self.assertTrue(self.driver.find_element(By.ID, "center_column"))
        nodes = self.driver.find_elements(By.XPATH, "//ul[@class='product_list grid row']/li")
        self.assertEqual(len(nodes), 5)
        # print(len(nodes))
        # time.sleep(20)

    def test_registration_success(self):
        # authorization header: sign in button
        self.driver.find_element(By.XPATH, "//a[@class='login']").click()

        # authorization page: email field
        self.driver.find_element(By.ID, "email_create").send_keys("otsfake+04@gmail.com")
        self.driver.find_element(By.ID, "SubmitCreate").click()
        # registration form: data fields and buttons
        self.assertTrue(self.driver.title == 'Login - My Store')
        self.driver.find_element(By.ID, "id_gender1").click()
        self.driver.find_element(By.ID, "customer_firstname").send_keys("firstName")
        self.driver.find_element(By.ID, "customer_lastname").send_keys("LastName")
        self.driver.find_element(By.ID, "passwd").send_keys("Test123")

        self.select_days = Select(self.driver.find_element(By.ID, "days"))
        self.select_days.select_by_value("15")

        self.select_month = Select(self.driver.find_element(By.ID, "months"))
        self.select_month.select_by_value("1")

        self.select_year = Select(self.driver.find_element(By.ID, "years"))
        self.select_year.select_by_value("2000")

        self.driver.find_element(By.ID, "address1").send_keys("address 1")
        self.driver.find_element(By.ID, "city").send_keys("City")
        self.driver.find_element(By.ID, "address1").send_keys("address 1")

        self.select_state = Select(self.driver.find_element(By.ID, "id_state"))
        self.select_state.select_by_value("1")

        self.driver.find_element(By.ID, "postcode").send_keys("12123")
        self.driver.find_element(By.ID, "phone_mobile").send_keys("511111111")
        self.driver.find_element(By.ID, "submitAccount").click()
        # account page:
        self.assertTrue(self.driver.current_url == "http://automationpractice.com/index.php?controller=my-account")
        # authorization page: user name displayed and logout button
        self.assertTrue(self.driver.find_element(By.XPATH, "//span[text()='firstName LastName']"))
        self.driver.find_element(By.XPATH, "//*[@title='Log me out']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//*[@title='Log in to your customer account']"))

        # time.sleep(5)

    def test_add_to_cart(self):
        # search field: send keys & button
        self.driver.find_element(By.ID, "search_query_top").send_keys("Dress")
        self.driver.find_element(By.XPATH, "//button[@name='submit_search']").click()
        time.sleep(5)
        # search page: change view icon
        self.driver.find_element(By.CLASS_NAME, "icon-th-list").click()
        self.assertTrue(self.driver.find_element(By.ID, "center_column"))
        nodes = self.driver.find_elements(By.XPATH, "//ul[@class='product_list row list']/li")
        self.assertTrue(len(nodes) > 0)
        # add to cart function: buttons, modal, shopping cart, shopping cart element
        self.driver.find_element(By.XPATH, "//span[text()='Add to cart']").click()
        self.assertTrue(self.driver.find_element(By.ID, "layer_cart"))
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@title='Continue shopping']/span").click()

        self.hover_cart = self.driver.find_element(By.XPATH, "//a[@title='View my shopping cart']")
        self.action = ActionChains(self.driver)
        self.action.move_to_element(self.hover_cart)
        time.sleep(3)
        self.action.perform()
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".products > .first_item"))

        self.hover_checkout_button = self.driver.find_element(By.CSS_SELECTOR, "#button_order_cart")
        self.action.click(self.hover_checkout_button)
        self.action.perform()
        # order page
        self.assertTrue(self.driver.current_url == "http://automationpractice.com/index.php?controller=order")
        self.quantity = self.driver.find_element(By.CSS_SELECTOR, ".cart_quantity_input").get_attribute("value")
        self.assertEquals(int(self.quantity), 1)
        print(self.quantity)


if __name__ == '_main_':
    unittest.main()
