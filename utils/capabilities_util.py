from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(browser: str):
    if browser.upper() == "CH":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser.upper() == "CH_HL":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    else:
        raise KeyError(
            f"Unexpected browser '{browser.upper()}'. Check your behave.ini variables")
    driver.set_window_size(1440, 900)
    return driver
