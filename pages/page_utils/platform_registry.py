from typing import Type

from pages.home_pages.hudl_home_page          import HudlHomePage
from pages.home_pages.wyscout_home_page       import WyscoutHomePage
from pages.home_pages.volleymetrics_home_page import VolleyMetricsHomePage
from pages.home_pages.wimu_home_page          import WimuHomePage
from pages.home_pages.home_page_base          import HomePageBase

PLATFORM_HOME_PAGES: dict[str, Type[HomePageBase]] = {
    "hudl":          HudlHomePage,
    "wyscout":       WyscoutHomePage,
    "volleymetrics": VolleyMetricsHomePage,
    "wimu cloud":    WimuHomePage,
}


def get_home_page_class(platform: str) -> Type[HomePageBase]:
    try:
        return PLATFORM_HOME_PAGES[platform.lower()]
    except KeyError as exc:
        raise ValueError(
            f'Unknown platform "{platform}". '
            "Add it to pages.page_utils.platform_registry.PLATFORM_HOME_PAGES."
        ) from exc