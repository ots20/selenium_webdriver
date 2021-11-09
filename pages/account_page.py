from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    __ACCOUNT_PAGE_URL = 'http://automationpractice.com/index.php?controller=my-account'

    def check_account_page(self):
        if self.get_current_url() == self.__ACCOUNT_PAGE_URL:
            return True
