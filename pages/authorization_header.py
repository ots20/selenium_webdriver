from selenium.webdriver.common.by import By


class AuthorizationHeader:

    def __init__(self, driver):
        self.driver = driver

    __SIGN_IN_BUTTON = (By.XPATH, "//a[@class='login']")
    __USER_NAME = (By.XPATH, "//span[text()='firstName LastName']")
    __LOG_OUT_BUTTON = (By.XPATH, "//*[@title='Log me out']")

    def click_sign_in(self):
        self.driver.find_element(self.__SIGN_IN_BUTTON).click()

    def check_user_name_account_page(self):
        return self.driver.find_element(self.__USER_NAME)

    def logout(self):
        self.driver.find_element(self.__LOG_OUT_BUTTON).click()
        return self.driver.find_element(self.__SIGN_IN_BUTTON)





