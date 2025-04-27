from selenium.webdriver.common.by import By
from pages.home_pages.home_page_base import HomePageBase

class WimuHomePage(HomePageBase):
    URL = "https://app.wimucloud.com"
    HOME_PAGE_TITLE = "WIMU PRO CLOUD"

    def check_page_loaded(self) -> bool:
        self.wait_for_title_to_match(self.HOME_PAGE_TITLE)
        return True
