from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthorizationHeader(BasePage):

    __SIGN_IN_BUTTON = (By.XPATH, "//a[@class='login']")
    __USER_NAME = (By.XPATH, "//span[text()='firstName LastName']")
    __LOG_OUT_BUTTON = (By.XPATH, "//*[@title='Log me out']")

    def check_sign_in_is_displayed(self):
        return self.get_element(self.__SIGN_IN_BUTTON)

    def click_sign_in(self):
        self.click(self.__SIGN_IN_BUTTON)

    def check_user_name_account_page(self):
        return self.get_element(self.__USER_NAME)

    def logout(self):
        self.click(self.__LOG_OUT_BUTTON)
        return self.get_element(self.__SIGN_IN_BUTTON)





