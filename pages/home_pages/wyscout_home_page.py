from selenium.webdriver.common.by import By
from pages.home_pages.home_page_base import HomePageBase

class WyscoutHomePage(HomePageBase):
    URL = "https://wyscout.hudl.com/"
    WELCOME_HEADING = (By.CSS_SELECTOR, "h2.headline.uni-headline--wy.page-title")
    EXPECTED_COPY = "Wyscout Subscription Required"

    def check_page_loaded(self) -> bool:
        return self.element_contains_copy(
            *self.WELCOME_HEADING,
            self.EXPECTED_COPY
        )
