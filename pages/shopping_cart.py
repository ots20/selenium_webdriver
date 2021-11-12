from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ShoppingCart(BasePage):

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

    # method not used
    def hover_on_cart2(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.__HOVERING_CART)).perform()

    def hover_on_cart(self):
        self.hover_element(self.__HOVERING_CART)

    def check_product_in_hover(self):
        return self.get_element(self.__PRODUCT_IN_CART)

    def click_checkout_button(self):
        self.click(self.__CART_CHECKOUT_BUTTON)
