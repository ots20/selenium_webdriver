from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchField(BasePage):

    __SEARCH_FIELD = (By.ID, "search_query_top")
    __ELASTIC_SEARCH = (By.CSS_SELECTOR, ".ac_results > ul > li")
    __SEARCH_BUTTON = (By. XPATH, "//button[@name='submit_search']")

    def search_item(self):
        self.fill(self.__SEARCH_FIELD, "Printed dress")

    def elastic_search_check(self):
        return self.get_the_elements(self.__ELASTIC_SEARCH)

    def click_search_icon(self):
        self.click(self.__SEARCH_BUTTON)