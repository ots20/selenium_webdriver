from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegistrationForm:

    def __init__(self, driver):
        self.driver = driver


def fill_registration_form(self):
    self.driver.find_element(By.ID, "id_gender1").click()
    self.driver.find_element(By.ID, "customer_firstname").send_keys("firstName")
    self.driver.find_element(By.ID, "customer_lastname").send_keys("LastName")
    self.driver.find_element(By.ID, "passwd").send_keys("Test123")

    Select(self.driver.find_element(By.ID, "days")).select_by_value("15")
    Select(self.driver.find_element(By.ID, "months")).select_by_value("1")
    Select(self.driver.find_element(By.ID, "years")).select_by_value("2000")

    self.driver.find_element(By.ID, "address1").send_keys("address 1")
    self.driver.find_element(By.ID, "city").send_keys("City")
    self.driver.find_element(By.ID, "address1").send_keys("address 1")

    Select(self.driver.find_element(By.ID, "id_state")).select_by_value("1")
    self.driver.find_element(By.ID, "postcode").send_keys("12123")
    self.driver.find_element(By.ID, "phone_mobile").send_keys("511111111")
    self.driver.find_element(By.ID, "submitAccount").click()
