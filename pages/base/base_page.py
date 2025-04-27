from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver  = driver
        self.timeout = timeout

    def wait_for_element_visible(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def wait_for_element_clickable(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((by, locator))
        )

    def element_contains_copy(self, by, locator, expected_text) -> bool:
        try:
            elem = self.wait_for_element_visible(by, locator)
            actual_text = elem.text.strip()
            return actual_text == expected_text
        except TimeoutException:
            return False

    def wait_for_title_to_match(self, expected_title):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.title_is(expected_title)
        )

    def click_element(self, by, locator):
        return self.wait_for_element_clickable(by, locator).click()
