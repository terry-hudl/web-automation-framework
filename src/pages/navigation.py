from typing import Dict, Tuple, Union
from selenium.webdriver.common.by import By

from src.pages.base_page  import BasePage
from src.domain.platform  import Platform


class NavMenu(BasePage):
    _LOGIN_DROPDOWN = (By.CSS_SELECTOR, 'a[data-qa-id="login-select"]')

    _PLATFORM_LOCATORS: Dict[Platform, Tuple] = {
        Platform.HUDL:          (By.CSS_SELECTOR, 'a[data-qa-id="login-hudl"]'),
        Platform.WYSCOUT:       (By.CSS_SELECTOR, 'a[data-qa-id="login-wyscout"]'),
        Platform.VOLLEYMETRICS: (By.CSS_SELECTOR, 'a[data-qa-id="login-volleymetrics"]'),
        Platform.WIMU_CLOUD:    (By.CSS_SELECTOR, 'a[data-qa-id="login-wimu"]'),
    }

    def open_dropdown(self) -> None:
        self.click(*self._LOGIN_DROPDOWN)

    def choose_platform(self, platform: Union[str, Platform]) -> None:
        if isinstance(platform, str):
            platform = Platform(platform.lower())

        try:
            self.click(*self._PLATFORM_LOCATORS[platform])
        except KeyError as err:
            raise ValueError(f"No locator registered for {platform}") from err

    def verify_login_options(self) -> list[str]:
        missing: list[str] = []
        for p, loc in self._PLATFORM_LOCATORS.items():
            try:
                self._visible(loc)
            except Exception:
                missing.append(p.value.title())
        return missing
