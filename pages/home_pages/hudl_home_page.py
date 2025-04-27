from selenium.webdriver.common.by import By
from pages.home_pages.home_page_base import HomePageBase

class HudlHomePage(HomePageBase):
    URL = "https://www.hudl.com/home"
    HOME_CONTENT = (By.ID, 'home-content')

    def check_page_loaded(self) -> bool:
        self.wait_for_element_visible(*self.HOME_CONTENT)
        return True
