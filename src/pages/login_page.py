from selenium.webdriver.common.by import By
from selenium.common.exceptions   import TimeoutException
from src.pages.base_page   import BasePage
from src.domain.credentials import Credentials
from src.pages.login_page_ids     import LoginPageid


class LoginPage(BasePage):
    _USERNAME = (By.ID,          "username")
    _CONTINUE = (By.CSS_SELECTOR, "button._button-login-id")
    _PASSWORD = (By.NAME,        "password")
    _LOGIN    = (By.CSS_SELECTOR, 'button[data-action-button-primary="true"]')
    _ERROR    = (By.ID,          "error-element-password")

    PAGE_ID = LoginPageid.LOGIN_FORM

    def is_loaded(self) -> bool:
        by, selector = self.PAGE_ID.locator()
        return self.text_matches("", by, selector)

    def log_in(self, creds: Credentials) -> None:
        if not self.is_loaded():
            raise RuntimeError("Login form failed to load")
        self.type(creds.username, *self._USERNAME)
        self.click(*self._CONTINUE)
        self.type(creds.password, *self._PASSWORD)
        self.click(*self._LOGIN)

    def is_error_displayed(self) -> bool:
        try:
            self._visible(self._ERROR)
            return True
        except TimeoutException:
            return False
