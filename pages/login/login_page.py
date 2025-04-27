from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage
from pages.page_utils.login_page_id_registry import get_page_id, LoginPageIdentifiers


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button._button-login-id")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[data-action-button-primary="true"]')
    ERROR_MESSAGE = (By.ID, "error-element-password")

    PAGE_ID: LoginPageIdentifiers = get_page_id("login_form")

    def is_page_loaded(self) -> bool:
        by, locator, _ = self.PAGE_ID
        try:
            if by is None:
                return self.driver.title == locator
            self.wait_for_element_visible(by, locator)
            return True
        except Exception:
            return False

    def enter_username(self, username: str):
        self.wait_for_element_visible(*self.USERNAME_INPUT).send_keys(username)
        # self.click_element(*self.CONTINUE_BUTTON)

    def submit_email(self):
        # self.wait_for_element_visible(*self.USERNAME_INPUT).send_keys(username)
        self.click_element(*self.CONTINUE_BUTTON)

    def enter_password(self, password: str):
        self.wait_for_element_visible(*self.PASSWORD_INPUT).send_keys(password)

    def submit_login(self):
        self.click_element(*self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        if not self.is_page_loaded():
            raise RuntimeError("Login page did not load correctly.")
        self.enter_username(username)
        self.submit_email()
        self.enter_password(password)
        self.submit_login()

    def is_error_displayed(self) -> bool:
        try:
            self.wait_for_element_visible(*self.ERROR_MESSAGE)
            return True
        except Exception:
            return False

