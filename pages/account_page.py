from pages.base_page import BasePage


class AccountPage(BasePage):

    __ACCOUNT_PAGE_URL = 'http://automationpractice.com/index.php?controller=my-account'

    def check_account_page(self):
        if self.get_current_url(self.__ACCOUNT_PAGE_URL) == self.__ACCOUNT_PAGE_URL:
            return True
