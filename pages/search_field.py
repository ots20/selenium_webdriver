from selenium.webdriver.common.by import By


class SearchField:

    def __init__(self, driver):
        self.driver = driver

    __SEARCH_FIELD = (By.ID, "search_query_top")
    __ELASTIC_SEARCH = (By.CSS_SELECTOR, ".ac_results > ul > li")
    __SEARCH_BUTTON = (By. XPATH, "//button[@name='submit_search']")

    def search_item(self):
        self.driver.find_element(*self.__SEARCH_FIELD).send_keys("Printed dress")

    def elastic_search_check(self):
        return self.driver.find_elements(*self.__ELASTIC_SEARCH)

    def click_search_icon(self):
        self.driver.find_element(*self.__SEARCH_BUTTON).click()
