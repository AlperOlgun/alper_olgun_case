from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JobsPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_page_loaded(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def verify_jobs_listed(self):
        page_source = self.driver.page_source.lower()
        assert "quality assurance" in page_source or "qa" in page_source, \
            "QA-related content was not found on the page."