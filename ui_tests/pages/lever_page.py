from pages.base_page import BasePage


class LeverPage(BasePage):
    def verify_redirected_to_lever(self):
        url = self.current_url()
        assert "lever.co" in url.lower(), f"Not redirected to Lever. Current URL: {url}"