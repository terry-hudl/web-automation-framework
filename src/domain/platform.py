from __future__ import annotations

from enum import Enum, unique
from typing import Dict, Type, TYPE_CHECKING

if TYPE_CHECKING:               # type hints only
    from src.pages.home_pages.base import HomePageBase


@unique
class Platform(str, Enum):
    HUDL          = "hudl"
    WYSCOUT       = "wyscout"
    VOLLEYMETRICS = "volleymetrics"
    WIMU_CLOUD    = "wimu cloud"


_HOME_PAGES: Dict[Platform, Type["HomePageBase"]] = {}


def register(platform: Platform):
    def _wrapper(cls: Type["HomePageBase"]):
        _HOME_PAGES[platform] = cls
        return cls
    return _wrapper


# ------------------------------------------------------------------
# Eagerly load *all* home-page modules so their decorators execute.
# This must come *after* the enum and decorator are defined.
# ------------------------------------------------------------------

import importlib  # (import after definitions is intentional)

import src.pages.home_pages # triggers the imports listed in its __init__


# ------------------------------------------------------------------
# Public helper
# ------------------------------------------------------------------

def get_home_page_class(platform: Platform) -> Type["HomePageBase"]:
    try:
        return _HOME_PAGES[platform]
    except KeyError as err:
        raise ValueError(f"No HomePage registered for platform {platform}") from err
