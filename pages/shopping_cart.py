from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ShoppingCart:

    def __init__(self, driver):
        self.driver = driver

    __PRODUCT_IN_CART = (By.CSS_SELECTOR, ".products > .first_item")
    __ADD_TO_CART_BUTTON = (By.XPATH, "//span[text()='Add to cart']")
    __CART_POPUP = (By.ID, "layer_cart")
    __CLOSE_CART_POPUP = (By.XPATH, "//*[@title='Continue shopping']/span")
    __HOVERING_CART = (By.XPATH, "//a[@title='View my shopping cart']")
    __CART_CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#button_order_cart")

    def add_to_cart(self):
        self.driver.find_element(*self.__ADD_TO_CART_BUTTON).click()
        return self.driver.find_element(*self.__CART_POPUP)

    def close_cart_popup(self):
        self.driver.find_element(*self.__CLOSE_CART_POPUP).click()

    # CHECK IF THIS WORKS!!
    def asserting(self, element):
        return self.driver.find_element(*element)

    # Check if the assert works
    def hover_on_cart(self):
        # hover_cart = self.driver.find_element(*self.__HOVERING_CART)
        action = ActionChains(self.driver)
        # action.move_to_element(hover_cart)
        action.move_to_element(self.driver.find_element(*self.__HOVERING_CART)).perform()
        print(self.driver.find_element(*self.__HOVERING_CART).get_attribute("title"))
        # return self.driver.find_element(By.CSS_SELECTOR, ".products > .first_item")
        # if not self.asserting(self.__PRODUCT_IN_CART):
        #     return

    def check_product_in_hover(self):
        return self.driver.find_element(*self.__PRODUCT_IN_CART)

    def click_checkout_button(self):
        self.driver.find_element(*self.__CART_CHECKOUT_BUTTON).click()
