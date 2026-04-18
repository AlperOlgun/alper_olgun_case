from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def create_driver(browser_name: str):
    browser_name = browser_name.lower()

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(0)
    return driver