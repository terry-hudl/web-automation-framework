from utils.config import config
from pages.base.base_page import BasePage
from pages.navigation.nav_menu import NavMenu

class HudlLandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{config['base_url']}/"
        self.nav_menu = NavMenu(driver)

    def load(self):
        self.driver.get(self.url)

    def __getattr__(self, item):
        return getattr(self.nav_menu, item)
