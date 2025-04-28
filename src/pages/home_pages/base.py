from abc import ABC, abstractmethod
from src.pages.base_page import BasePage


class HomePageBase(BasePage, ABC):
    @property
    @abstractmethod
    def URL(self) -> str: ...

    @abstractmethod
    def _loaded_locator(self): ...

    # ───────────────────────────────────────────── #

    def load(self) -> None:
        self.driver.get(self.URL)

    def is_loaded(self) -> bool:
        try:
            self._visible(self._loaded_locator())
            return True
        except Exception:
            return False
