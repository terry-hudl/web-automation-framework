from behave import given, when, then
from pages.landing_page.global_hudl_landing_page import HudlLandingPage
from pages.login.login_page import LoginPage
from pages.page_utils.platform_registry import get_home_page_class
from utils.credentials import get_credentials
from pages.page_utils.page_factory import get_page

@given('I have chosen to login to the {platform} platform')
def step_navigate_to_login(context, platform):
    landing_page = get_page(context, HudlLandingPage)
    landing_page.load()
    landing_page.invoke_login()
    landing_page.invoke_platform_login(platform)

@then('the {platform} login form should be displayed')
def step_login_form_visible(context, platform):
    login_page = get_page(context, LoginPage)
    if not login_page.is_page_loaded():
        raise AssertionError(f"{platform} login page did not load as expected.")

@when('I login with "{login_type}" credentials')
@when('I login with invalid credentials ("{login_type}")')
def step_login_with_type(context, login_type):
    login_page = get_page(context, LoginPage)
    creds = get_credentials(login_type)
    login_page.login(creds['username'], creds['password'])


@then('I should successfully be logged in to the {platform} platform')
def step_verify_successful_login(context, platform):
    home_page = get_page(context, get_home_page_class(platform))

    if not home_page.is_page_loaded():
        raise AssertionError(
            f"Expected {platform} home page to be displayed."
        )

@then('I should not be logged in to the {platform} platform')
def step_verify_unsuccessful_login(context, platform):
    home_page = get_page(context, get_home_page_class(platform))

    if home_page.is_page_loaded():
        raise AssertionError(
            f"The {platform} Home page should not be displayed."
        )

@then('I should see login error message displayed')
def step_verify_unsuccessful_login(context):
    login_page = get_page(context, LoginPage)

    if not login_page.is_error_displayed():
        raise AssertionError(
            "No error message displayed for invalid login attempt."
        )