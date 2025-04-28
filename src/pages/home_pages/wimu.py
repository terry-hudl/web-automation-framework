from selenium.webdriver.common.by import By

from src.domain.platform       import Platform, register
from src.pages.home_pages.base import HomePageBase


@register(Platform.WIMU_CLOUD)
class WimuHomePage(HomePageBase):

    URL = "https://app.wimucloud.com"
    _EXPECTED_TITLE = "Hudl Signal"

    # Title-based check instead of locator
    def is_loaded(self) -> bool:
        try:
            return self.driver.title == self._EXPECTED_TITLE
        except Exception:
            return False

    def _loaded_locator(self):
        # Satisfy abstract contract; never used.
        return By.TAG_NAME, "html"
