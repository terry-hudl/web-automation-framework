from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base.base_page import BasePage


class NavMenu(BasePage):
    LOGIN_NAV_LINK = (By.CSS_SELECTOR, 'a[data-qa-id="login-select"]')

    HUDL_LOGIN_NAV_LINK = (By.CSS_SELECTOR, 'a[data-qa-id="login-hudl"]')
    WYSCOUT_LOGIN_NAV_LINK = (By.CSS_SELECTOR, 'a[data-qa-id="login-wyscout"]')
    VOLLYMETRICS_LOGIN_NAV_LINK = (By.CSS_SELECTOR, 'a[data-qa-id="login-volleymetrics"]')
    WIMU_CLOUD_LOGIN_NAV_LINK = (By.CSS_SELECTOR, 'a[data-qa-id="login-wimu"]')
    INSTAT_BASKETBALL_LOGIN_NAV_LINK = (By.CSS_SELECTOR, 'a[data-qa-id="login-instat-basketball"]')
    INSTAT_ICE_HOCKEY_LOGIN_NAV_LINK = (By.CSS_SELECTOR, 'a[data-qa-id="login-instat-icehockey"]')
    IQ_FOOTBALL_LOGIN_NAV_LINK = (By.CSS_SELECTOR, 'a[data-qa-id="login-wyscout"]')

    PLATFORM_METHODS = {
        'hudl': 'invoke_hudl_login',
        'wyscout': 'invoke_wyscout_login',
        'volleymetrics': 'invoke_volleymetrics_login',
        'wimu cloud': 'invoke_wimu_login',
    }

    def invoke_login(self):
        self.click_element(*self.LOGIN_NAV_LINK)

    def invoke_hudl_login(self):
        self.click_element(*self.HUDL_LOGIN_NAV_LINK)

    def invoke_wyscout_login(self):
        self.click_element(*self.WYSCOUT_LOGIN_NAV_LINK)

    def invoke_volleymetrics_login(self):
        self.click_element(*self.VOLLYMETRICS_LOGIN_NAV_LINK)

    def invoke_wimu_login(self):
        self.click_element(*self.WIMU_CLOUD_LOGIN_NAV_LINK)

    def invoke_platform_login(self, platform: str):
        key = platform.lower()
        method_name = self.PLATFORM_METHODS.get(key)
        if not method_name or not hasattr(self, method_name):
            raise ValueError(f"No login‐method defined for platform '{platform}'")
        getattr(self, method_name)()

    def verify_login_options(self) -> list[str]:
        options = {
            'Hudl': self.HUDL_LOGIN_NAV_LINK,
            'Wyscout': self.WYSCOUT_LOGIN_NAV_LINK,
            'Volleymetrics': self.VOLLYMETRICS_LOGIN_NAV_LINK,
            'Wimu Cloud': self.WIMU_CLOUD_LOGIN_NAV_LINK,
            'InStat Basketball': self.INSTAT_BASKETBALL_LOGIN_NAV_LINK,
            'InStat Ice Hockey': self.INSTAT_ICE_HOCKEY_LOGIN_NAV_LINK,
            'IQ Football': self.IQ_FOOTBALL_LOGIN_NAV_LINK,
        }

        missing = []
        for name, locator in options.items():
            try:
                self.wait_for_element_visible(*locator)
            except TimeoutException:
                missing.append(f'"{name}" login option not present')
        return missing
