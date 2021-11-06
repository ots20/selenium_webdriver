from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    __ACCOUNT_PAGE_URL = 'http://automationpractice.com/index.php?controller=my-account'

    def check_account_page(self):
        self.driver.current_url = self.__ACCOUNT_PAGE_URL

