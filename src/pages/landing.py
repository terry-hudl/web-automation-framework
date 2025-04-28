from typing import Union
from src.config.settings import settings
from src.pages.base_page  import BasePage
from src.pages.navigation import NavMenu
from src.domain.platform  import Platform


class HudlLandingPage(BasePage):
    _url = f"{settings.base_url}/"

    def __init__(self, driver, timeout: int = BasePage.timeout):
        super().__init__(driver, timeout)
        self.nav = NavMenu(driver, timeout)

    def load(self) -> None:
        self.driver.get(self._url)

    def open_login_dropdown(self):
        self.nav.open_dropdown()

    def choose_platform(self, platform: Union[str, Platform]):
        self.nav.choose_platform(platform)

    def verify_login_options(self):
        return self.nav.verify_login_options()
