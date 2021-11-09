from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ShoppingCart(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    __PRODUCT_IN_CART = (By.CSS_SELECTOR, ".products > .first_item")
    __ADD_TO_CART_BUTTON = (By.XPATH, "//span[text()='Add to cart']")
    __CART_POPUP = (By.ID, "layer_cart")
    __CLOSE_CART_POPUP = (By.XPATH, "//*[@title='Continue shopping']/span")
    __HOVERING_CART = (By.XPATH, "//a[@title='View my shopping cart']")
    __CART_CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#button_order_cart")

    def add_to_cart(self):
        self.click(self.__ADD_TO_CART_BUTTON)
        return self.get_element(self.__CART_POPUP)

    def close_cart_popup(self):
        self.click(self.__CLOSE_CART_POPUP)

    # CHECK IF THIS WORKS!!
    def asserting(self, element):
        return self.get_element(element)

    # Check if the assert works
    def hover_on_cart(self):
        # hover_cart = self.driver.find_element(*self.__HOVERING_CART)
        action = ActionChains(self.driver)
        # action.move_to_element(hover_cart)
        action.move_to_element(self.driver.find_element(*self.__HOVERING_CART)).perform()
        print(self.driver.find_element(*self.__HOVERING_CART).get_attribute("title"))

    def hover_2(self):
        # self.hover_element(self.__HOVERING_CART)
        self.hover_element(self.__HOVERING_CART)

    def check_product_in_hover(self):
        return self.get_element(self.__PRODUCT_IN_CART)

    def click_checkout_button(self):
        self.click(self.__CART_CHECKOUT_BUTTON)
        # self.hover_click(self.__CART_CHECKOUT_BUTTON)

    def temp_find_element(self):
        return self.get_element(self.__HOVERING_CART)