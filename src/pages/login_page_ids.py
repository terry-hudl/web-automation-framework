from enum import Enum
from selenium.webdriver.common.by import By

class LoginPageid(Enum):
    HUDL_HOME       = (By.ID, "home-content", "Hudl home")
    WYSCOUT_HOME    = (By.CSS_SELECTOR, "h2.headline.uni-headline--wy.page-title", "Wyscout home")
    VOLLEYMETRICS   = (By.CSS_SELECTOR, "span.sandbox-heading-1", "VolleyMetrics home")
    WIMU_CLOUD      = (None, "WIMU PRO CLOUD", "WIMU Cloud title")
    LOGIN_FORM      = (By.ID, "username", "Universal login form")

    def locator(self):
        return self.value[:2]
