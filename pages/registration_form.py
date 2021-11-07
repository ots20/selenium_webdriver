from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class RegistrationForm(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    __GENDER_SELECT = (By.ID, "id_gender1")
    __FIRST_NAME = (By.ID, "customer_firstname")
    __LAST_NAME = (By.ID, "customer_lastname")
    __REG_PASSWORD = (By.ID, "passwd")
    __BIRTH_DAY = (By.ID, "days")
    __BIRTH_MONTH = (By.ID, "months")
    __BIRTH_YEAR = (By.ID, "years")
    __ADDRESS_MAIN = (By.ID, "address1")
    __ADDRESS_CITY = (By.ID, "city")
    __DROPDOWN_STATE = (By.ID, "id_state")
    __ZIP_CODE = (By.ID, "postcode")
    __PHONE = (By.ID, "phone_mobile")
    __REG_SUBMIT_BUTTON = (By.ID, "submitAccount")

    def fill_registration_form(self):
        self.driver.find_element(*self.__GENDER_SELECT).click()
        self.driver.find_element(*self.__FIRST_NAME).send_keys("firstName")
        self.driver.find_element(*self.__LAST_NAME).send_keys("LastName")
        self.driver.find_element(*self.__REG_PASSWORD).send_keys("Test123")

        Select(self.driver.find_element(*self.__BIRTH_DAY)).select_by_value("15")
        Select(self.driver.find_element(*self.__BIRTH_MONTH)).select_by_value("1")
        Select(self.driver.find_element(*self.__BIRTH_YEAR)).select_by_value("2000")

        self.driver.find_element(*self.__ADDRESS_MAIN).send_keys("address 1")
        self.driver.find_element(*self.__ADDRESS_CITY).send_keys("City")

        Select(self.driver.find_element(*self.__DROPDOWN_STATE)).select_by_value("1")
        self.driver.find_element(*self.__ZIP_CODE).send_keys("12123")
        self.driver.find_element(*self.__PHONE).send_keys("511111111")
        self.driver.find_element(*self.__REG_SUBMIT_BUTTON).click()
