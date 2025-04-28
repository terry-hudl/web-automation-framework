from behave import given, when
from src.core.page_factory        import get_page
from src.domain.platform          import Platform, get_home_page_class
from src.pages.landing            import HudlLandingPage


@given('I have opened the Hudl platform')
def step_open_hudl(context):
    landing: HudlLandingPage = get_page(context, HudlLandingPage)
    landing.load()


@when('I navigate directly to the {platform} home page')
def step_navigate_directly(context, platform):
    home_cls = get_home_page_class(Platform(platform.lower()))
    home     = get_page(context, home_cls)
    home.load()
