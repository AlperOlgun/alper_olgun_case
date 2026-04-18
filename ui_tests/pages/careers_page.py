from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersPage(BasePage):
    URL = "https://insiderone.com/careers/#open-roles"

    SEE_ALL_TEAMS_BUTTON = (By.XPATH, "//*[self::a or self::button or self::div][contains(normalize-space(.), 'See all teams')]")
    QA_TEAM_LINK = (By.XPATH, "//*[contains(normalize-space(.), 'Quality Assurance')]")

    def load(self):
        self.open(self.URL)

    def click_see_all_teams(self):
        self.click(self.SEE_ALL_TEAMS_BUTTON)

    def select_quality_assurance_team(self):
        self.scroll_into_view(self.QA_TEAM_LINK)
        self.click(self.QA_TEAM_LINK)