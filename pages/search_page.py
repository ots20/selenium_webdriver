from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    __PAGE_TITLE = 'Search - My Store'
    __RESULT_SECTION = (By.ID, "center_column")
    __LIST_VIEW = (By.CLASS_NAME, "icon-th-list")
    __ITEMS_FOUND_NUMBER = (By.XPATH, "//ul[@class='product_list row list']/li")

    def check_page_title(self):
        return self.driver.title == self.__PAGE_TITLE

    def check_search_results_section(self):
        return self.driver.find_element(self.__RESULT_SECTION)

    def results_found_number(self):
        self.driver.find_element(self.__LIST_VIEW).click()
        return self.driver.find_elements(self.__ITEMS_FOUND_NUMBER)


