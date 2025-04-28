from behave import given, when, then
from src.core.page_factory        import get_page
from src.domain.credentials       import CredentialType, get_credentials
from src.domain.platform          import Platform, get_home_page_class
from src.pages.landing            import HudlLandingPage
from src.pages.login_page         import LoginPage

@given('I have chosen to login to the {platform} platform')
def step_choose_platform_login(context, platform: str):
    landing: HudlLandingPage = get_page(context, HudlLandingPage)
    landing.load()
    landing.open_login_dropdown()
    landing.choose_platform(Platform(platform.lower()))

@when('I login with "{cred_kind}" credentials')
@when('I login with invalid credentials ("{cred_kind}")')
def step_login_with_credentials(context, cred_kind):
    login: LoginPage = get_page(context, LoginPage)
    creds = get_credentials(CredentialType(cred_kind.lower()))
    login.log_in(creds)

@then('the {platform} login form should be displayed')
def step_login_form_displayed(context, platform):
    login: LoginPage = get_page(context, LoginPage)
    assert login.is_loaded(), f"{platform} login form did not appear."

@then('I should successfully be logged in to the {platform} platform')
def step_verify_successful_login(context, platform):
    home_cls = get_home_page_class(Platform(platform.lower()))
    home     = get_page(context, home_cls)
    assert home.is_loaded(), f"Expected {platform} home page, but it was not loaded."

@then('I should not be logged in to the {platform} platform')
def step_verify_not_logged_in(context, platform):
    home_cls = get_home_page_class(Platform(platform.lower()))
    home     = get_page(context, home_cls)
    assert not home.is_loaded(), f"{platform} home page should NOT be visible."

@then('I should see login error message displayed')
def step_error_message_displayed(context):
    login: LoginPage = get_page(context, LoginPage)
    assert login.is_error_displayed(), "No error message shown for invalid login."
