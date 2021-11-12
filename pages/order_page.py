from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):

    __ORDER_URL = "http://automationpractice.com/index.php?controller=order"
    __ORDER_PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity_input")

    def check_url(self):
        if self.get_current_url(self.__ORDER_URL) == self.__ORDER_URL:
            return True

    def check_product_quantity(self):
        quantity = self.get_element_attribute(self.__ORDER_PRODUCT_QUANTITY, 'value')
        return int(quantity)
