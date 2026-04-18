from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_login_page_open():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        time.sleep(2)

        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        login_button.click()

        time.sleep(2)

        success_message = driver.find_element(By.ID, "flash").text
        assert "You logged into a secure area!" in success_message

    finally:
        driver.quit()
        
def test_login_negative():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username.send_keys("wrong_user")
        password.send_keys("wrong_pass")
        login_button.click()

        wait = WebDriverWait(driver, 10)
        error_message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text

        assert "Your username is invalid!" in error_message

    finally:
        driver.quit()