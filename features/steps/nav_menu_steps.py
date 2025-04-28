from behave import when, then
from src.core.page_factory        import get_page
from src.domain.platform          import Platform
from src.pages.landing            import HudlLandingPage


@when('I open the login options within the nav menu')
def step_open_login_dropdown(context):
    landing: HudlLandingPage = get_page(context, HudlLandingPage)
    landing.open_login_dropdown()

@when('I initiate logging in to the {platform} platform')
def step_initiate_platform_login(context, platform):
    landing: HudlLandingPage = get_page(context, HudlLandingPage)
    landing.choose_platform(Platform(platform.lower()))


@then('I should have options to login to different Hudl areas')
def step_verify_login_options(context):
    landing: HudlLandingPage = get_page(context, HudlLandingPage)
    missing = landing.verify_login_options()
    assert not missing, (
        "These expected login options were absent:\n  " + "\n  ".join(missing)
    )
