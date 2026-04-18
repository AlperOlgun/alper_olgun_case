from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://insiderone.com/"

    COMPANY_MENU = (By.XPATH, "//a[contains(., 'Company')]")
    NAVBAR = (By.TAG_NAME, "header")
    FOOTER = (By.TAG_NAME, "footer")

    def load(self):
        self.open(self.URL)

    def verify_home_page_loaded(self):
        assert "Insider" in self.driver.title
        assert self.is_visible(self.NAVBAR), "Navbar is not visible"
        assert self.is_visible(self.FOOTER), "Footer is not visible"