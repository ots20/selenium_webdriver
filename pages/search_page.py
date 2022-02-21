from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):

    __PAGE_TITLE = 'Search - My Store'
    __RESULT_SECTION = (By.ID, "center_column")
    __LIST_VIEW = (By.CLASS_NAME, "icon-th-list")
    __ITEMS_FOUND_NUMBER = (By.XPATH, "//ul[@class='product_list row list']/li")

    def check_page_title(self):
        return self.get_page_title(self.__PAGE_TITLE) == self.__PAGE_TITLE

    def check_search_results_section(self):
        return self.get_element(self.__RESULT_SECTION)

    def results_found_number(self):
        self.click(self.__LIST_VIEW)
        return self.get_the_elements(self.__ITEMS_FOUND_NUMBER)



