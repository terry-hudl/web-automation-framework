from selenium.webdriver.common.by import By
from pages.home_pages.home_page_base import HomePageBase

class VolleyMetricsHomePage(HomePageBase):
    URL = "https://portal.volleymetrics.hudl.com"
    WELCOME_HEADING = (By.CSS_SELECTOR, "span.sandbox-heading-1")
    EXPECTED_COPY = "Welcome to the VolleyMetrics Portal!"

    def check_page_loaded(self) -> bool:
        return self.element_contains_copy(
            *self.WELCOME_HEADING,
            self.EXPECTED_COPY
        )
