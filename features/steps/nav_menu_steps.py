from behave import when, then
from pages.landing_page.global_hudl_landing_page import HudlLandingPage
from pages.page_utils.page_factory import get_page

@when('I open the login options within the nav menu')
def step_open_login_options(context):
    landing_page = get_page(context, HudlLandingPage)
    landing_page.invoke_login()

@when('I initiate logging in to the {platform} platform')
def step_initiate_login(context, platform: str) -> None:
    landing_page = get_page(context, HudlLandingPage)
    landing_page.invoke_platform_login(platform)

@then('I should have options to login to different Hudl areas')
def step_verify_login_options(context):
    landing = get_page(context, HudlLandingPage)
    missing = landing.verify_login_options()
    if missing:
        raise AssertionError("Some login options were missing:\n  " + "\n  ".join(missing))