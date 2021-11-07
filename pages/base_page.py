from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def fill(self, by_locator, value):
        self.driver.find_element(*by_locator).send_keys(value)

    def hover_element(self, by_locator):
        hover_element = self.driver.find_element(*by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(hover_element)
        action.perform()

