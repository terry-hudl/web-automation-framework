from selenium.common.exceptions import TimeoutException
from pages.base.base_page import BasePage

class HomePageBase(BasePage):
    URL: str = None

    def load(self) -> None:
        if not self.URL:
            raise NotImplementedError(
                f"{self.__class__.__name__} has no URL defined."
            )
        self.driver.get(self.URL)

    def is_page_loaded(self) -> bool:
        try:
            return self.check_page_loaded()
        except TimeoutException:
            return False

    def check_page_loaded(self) -> bool:
        raise NotImplementedError("Subclasses must override check_page_loaded method.")