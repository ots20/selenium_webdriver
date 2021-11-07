from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:

    class __WebDriver:
        def __init__(self):
            # s = Service(ChromeDriverManager().install())
            # self.driver = webdriver.Chrome(service=s)
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            self.driver.implicitly_wait(15)
            self.driver.maximize_window()

    driver = None

    def __init__(self):
        if not self.driver:
            BasePage.driver = BasePage.__WebDriver().driver

    def quit_driver(self):
        self.driver.quit()

    def go_to_url(self, url):
        self.driver.get(url)

    def get_page_title(self):
        return self.driver.title

    def get_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def get_the_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def fill(self, by_locator, value):
        self.driver.find_element(*by_locator).send_keys(value)

    def hover_element(self, by_locator):
        hover_element = self.driver.find_element(*by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(hover_element)
        action.perform()

