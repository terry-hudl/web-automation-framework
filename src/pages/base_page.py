from __future__ import annotations

from dataclasses import dataclass
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui       import WebDriverWait
from selenium.webdriver.support           import expected_conditions as EC
from selenium.common.exceptions           import TimeoutException

from src.config.settings import settings
from src.core.wait_protocol import Locator


@dataclass
class BasePage:
    driver:  WebDriver
    timeout: int = settings.timeout

    def _wait(self) -> WebDriverWait:
        return WebDriverWait(self.driver, self.timeout)

    def _visible(self, locator: Locator):
        return self._wait().until(EC.visibility_of_element_located(locator))

    def _clickable(self, locator: Locator):
        return self._wait().until(EC.element_to_be_clickable(locator))

    def click(self, *locator: Locator) -> None:
        self._clickable(locator).click()

    def type(self, text: str, *locator: Locator) -> None:
        element = self._visible(locator)
        element.clear()
        element.send_keys(text)

    def text_matches(self, expected: str, *locator: Locator) -> bool:
        try:
            return self._visible(locator).text.strip() == expected
        except TimeoutException:
            return False
