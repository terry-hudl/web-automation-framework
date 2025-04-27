from behave import given, when
from pages.landing_page.global_hudl_landing_page import HudlLandingPage
from pages.page_utils.platform_registry import get_home_page_class
from pages.page_utils.page_factory import get_page

@given('I have opened the Hudl platform')
def step_open_hudl(context):
    landing_page = get_page(context, HudlLandingPage)
    landing_page.load()

@when('I navigate directly to the {platform} home page')
def step_navigate_home_page(context, platform: str):
    home_page = get_page(context, get_home_page_class(platform))
    home_page.load()

