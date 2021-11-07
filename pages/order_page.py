from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    __ORDER_URL = "http://automationpractice.com/index.php?controller=order"
    __ORDER_PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity_input")

    def check_url(self):
        if self.driver.current_url == self.__ORDER_URL:
            return True

    def check_product_quantity(self):
        quantity = self.driver.find_element(*self.__ORDER_PRODUCT_QUANTITY).get_attribute("value")
        return int(quantity)
