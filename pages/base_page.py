from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:

    class __WebDriver:
        def __init__(self):
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            self.driver.maximize_window()
            # s = Service(ChromeDriverManager().install())
            # self.driver = webdriver.Chrome(service=s)

    driver = None

    def __init__(self):
        if not self.driver:
            BasePage.driver = BasePage.__WebDriver().driver
        self.explicitly_wait = WebDriverWait(driver=self.driver, timeout=5)

    def quit_driver(self):
        self.driver.quit()

    def go_to_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def get_element(self, by_locator):
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' element not present in the page")
        return self.driver.find_element(*by_locator)

    def get_the_elements(self, by_locator):
        self.explicitly_wait.until(expected_conditions.presence_of_all_elements_located(by_locator),
                                   message=f"'{by_locator}' elements not present in the page")
        return self.driver.find_elements(*by_locator)

    def click(self, by_locator):
        self.explicitly_wait.until(expected_conditions.element_to_be_clickable(by_locator),
                                   message=f"'{by_locator}' elements not present in the page")
        self.driver.find_element(*by_locator).click()

    def fill(self, by_locator, value):
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' elements not present in the page")
        self.driver.find_element(*by_locator).send_keys(value)

    def hover_element(self, by_locator):
        self.explicitly_wait.until(expected_conditions.element_to_be_clickable(by_locator),
                                   message=f"'{by_locator}' cannot hover over the element")
        hover_element = self.get_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(hover_element)
        action.perform()

    def hover_click(self, by_locator):
        self.explicitly_wait.until(expected_conditions.element_to_be_clickable(by_locator),
                                   message=f"'{by_locator}' cannot hover and click over the element")
        element_to_click = self.get_element(by_locator)
        action = ActionChains(self.driver)
        action.click(element_to_click)
        action.perform()

    def select_dropdown_value(self, by_locator, value):
        Select(self.get_element(by_locator)).select_by_value(value)

    def get_element_attribute(self, by_locator, attribute):
        return self.get_element(by_locator).get_attribute(attribute)

