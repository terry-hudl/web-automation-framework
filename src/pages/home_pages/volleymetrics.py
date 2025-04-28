from selenium.webdriver.common.by import By

from src.domain.platform       import Platform, register
from src.pages.home_pages.base import HomePageBase


@register(Platform.VOLLEYMETRICS)
class VolleyMetricsHomePage(HomePageBase):

    URL = "https://portal.volleymetrics.hudl.com"

    def _loaded_locator(self):
        return By.CSS_SELECTOR, "span.sandbox-heading-1"
