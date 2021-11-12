from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationForm(BasePage):

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
        self.click(self.__GENDER_SELECT)
        self.fill(self.__FIRST_NAME, "firstName")
        self.fill(self.__LAST_NAME, "LastName")
        self.fill(self.__REG_PASSWORD, "Test123")

        self.select_dropdown_value(self.__BIRTH_DAY, '15')
        self.select_dropdown_value(self.__BIRTH_MONTH, '1')
        self.select_dropdown_value(self.__BIRTH_YEAR, '2000')

        self.fill(self.__ADDRESS_MAIN, 'address 1')
        self.fill(self.__ADDRESS_CITY, 'City')

        self.select_dropdown_value(self.__DROPDOWN_STATE, '1')
        self.fill(self.__ZIP_CODE, '12345')
        self.fill(self.__PHONE, '511111111')
        self.click(self.__REG_SUBMIT_BUTTON)
