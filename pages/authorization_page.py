from selenium.webdriver.common.by import By


class AuthorizationPage:

    def __init__(self, driver):
        self.driver = driver

    def register_email(self):
        self.driver.find_element(By.ID, "email_create").send_keys("otsfake+07@gmail.com")
        self.driver.find_element(By.ID, "SubmitCreate").click()