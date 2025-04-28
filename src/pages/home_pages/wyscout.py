from selenium.webdriver.common.by import By

from src.domain.platform       import Platform, register
from src.pages.home_pages.base import HomePageBase


@register(Platform.WYSCOUT)
class WyscoutHomePage(HomePageBase):

    URL = "https://wyscout.hudl.com/"

    def _loaded_locator(self):
        return By.CSS_SELECTOR, "h2.headline.uni-headline--wy.page-title"
