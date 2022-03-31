from behave.runner import Context
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:

    def __init__(self, context: Context):
        self.driver = context.driver
        self.explicitly_wait = WebDriverWait(driver=self.driver, timeout=10)

    # ================= Private methods =================

    def __wait_element_to_be_visible(self, by_locator):
        self.explicitly_wait.until(expected_conditions.presence_of_all_elements_located(by_locator),
                                   message=f"'{by_locator}' element not present in the page")

    def __wait_multiple_elements_visibility(self, by_locator):
        self.explicitly_wait.until(expected_conditions.presence_of_all_elements_located(by_locator),
                                   message=f"'{by_locator}' those elements not present in the page")

    def __wait_element_to_be_clickable(self, by_locator):
        self.explicitly_wait.until(expected_conditions.element_to_be_clickable(by_locator),
                                   message=f"'{by_locator}' element not clickable in the page")

    def __wait_url_to_match(self, url):
        self.explicitly_wait.until(expected_conditions.url_to_be(url),
                                   message=f"'{url}' is not the expected URL")

    def __page_title_to_match(self, title):
        self.explicitly_wait.until(expected_conditions.title_is(title),
                                   message=f"'{title}' not expected title")

    def __wait_for_element_invisibility(self, by_locator):
        self.explicitly_wait.until(expected_conditions.invisibility_of_element(by_locator),
                                   message=f"'{by_locator}' popUp still visible!")

    # ================= Browser methods =================

    def quit_driver(self):
        self.driver.quit()

    def go_to_url(self, url):
        self.driver.get(url)

    def get_current_url(self, url):
        self.__wait_url_to_match(url)
        return self.driver.current_url

    def get_page_title(self, title):
        self.__page_title_to_match(title)
        return self.driver.title

    def get_element(self, by_locator):
        self.__wait_element_to_be_visible(by_locator)
        return self.driver.find_element(*by_locator)

    def get_the_elements(self, by_locator):
        self.__wait_multiple_elements_visibility(by_locator)
        return self.driver.find_elements(*by_locator)

    def click(self, by_locator):
        self.__wait_element_to_be_clickable(by_locator)
        self.driver.find_element(*by_locator).click()

    def fill(self, by_locator, value):
        self.__wait_element_to_be_visible(by_locator)
        self.driver.find_element(*by_locator).send_keys(value)

    def check_element_closed(self, by_locator):
        self.__wait_for_element_invisibility(by_locator)

    def hover_element(self, by_locator):
        self.__wait_element_to_be_clickable(by_locator)
        hover_element = self.get_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(hover_element)
        action.perform()

    def hover_click(self, by_locator):
        self.__wait_element_to_be_visible(by_locator)
        element_to_click = self.get_element(by_locator)
        action = ActionChains(self.driver)
        action.click(element_to_click)
        action.perform()

    def select_dropdown_value(self, by_locator, value):
        Select(self.get_element(by_locator)).select_by_value(value)

    def get_element_attribute(self, by_locator, attribute):
        element_attribute = self.get_element(by_locator).get_attribute(attribute)
        return element_attribute
