import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestSeleniumWebDriver(unittest.TestCase):

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(url="http://automationpractice.com/index.php")
        self.driver.implicitly_wait(6)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_search(self):
        self.driver.find_element(By.ID, "search_query_top").send_keys("Printed dress")
        # time.sleep(6)
        elastic_search = self.driver.find_elements(By.CSS_SELECTOR, ".ac_results > ul > li")
        self.assertEqual(len(elastic_search), 5)
        self.driver.find_element(By.XPATH, "//button[@name='submit_search']").click()
        self.assertTrue(self.driver.title == 'Search - My Store')
        self.assertTrue(self.driver.find_element(By.ID, "center_column"))
        nodes = self.driver.find_elements(By.XPATH, "//ul[@class='product_list grid row']/li")
        self.assertEqual(len(nodes), 5)
        # print(len(nodes))
        # time.sleep(20)



if __name__ == '_main_':
    unittest.main()
