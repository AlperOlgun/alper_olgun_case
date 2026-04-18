from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.jobs_page import JobsPage


def test_qa_jobs_flow(driver):
    home_page = HomePage(driver)
    careers_page = CareersPage(driver)
    jobs_page = JobsPage(driver)

    home_page.load()
    home_page.verify_home_page_loaded()

    careers_page.load()
    careers_page.click_see_all_teams()
    careers_page.select_quality_assurance_team()

    jobs_page.verify_page_loaded()
    jobs_page.verify_jobs_listed()