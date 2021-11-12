import string
import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthorizationPage(BasePage):

    __EMAIL_FIELD = (By.ID, "email_create")
    __SUBMIT_BUTTON = (By.ID, "SubmitCreate")
    __TAKEN_EMAIL_ERROR = (By.ID, "create_account_error")

    def register_email(self):
        letters = string.digits
        email_number = ''.join(random.choice(letters) for i in range(3))
        self.fill(self.__EMAIL_FIELD, 'otsfake7+{}@gmail.com'.format(email_number))
        self.click(self.__SUBMIT_BUTTON)
