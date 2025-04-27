from selenium.webdriver.common.by import By
from typing import Dict, NamedTuple


class LoginPageIdentifiers(NamedTuple):
    by: object
    locator: str
    description: str


PAGE_IDS: Dict[str, LoginPageIdentifiers] = {
    "hudl": LoginPageIdentifiers(By.ID, "home-content", "Hudl home"),
    "volleymetrics": LoginPageIdentifiers(
        By.CSS_SELECTOR, "span.sandbox-heading-1", "VolleyMetrics home"
    ),
    "wyscout": LoginPageIdentifiers(
        By.CSS_SELECTOR,
        "h2.headline.uni-headline--wy.page-title",
        "Wyscout subscription page",
    ),
    "wimu cloud": LoginPageIdentifiers(None, "WIMU PRO CLOUD", "WIMU Cloud title"),
    "login_form": LoginPageIdentifiers(By.ID, "username", "Universal login form"),
}


def get_page_id(name: str) -> LoginPageIdentifiers:
    try:
        return PAGE_IDS[name.lower()]
    except KeyError as exc:
        raise ValueError(f"No PageId mapping for '{name}'") from exc
