from selenium.webdriver.common.by import By

from src.domain.platform       import Platform, register
from src.pages.home_pages.base import HomePageBase


@register(Platform.HUDL)
class HudlHomePage(HomePageBase):

    URL = "https://www.hudl.com/home"

    def _loaded_locator(self):
        return By.ID, "home-content"
