from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all_visible(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except (ElementClickInterceptedException, TimeoutException):
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def is_visible(self, locator):
        try:
            self.find_visible(locator)
            return True
        except Exception:
            return False

    def scroll_into_view(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element

    def current_url(self):
        return self.driver.current_url