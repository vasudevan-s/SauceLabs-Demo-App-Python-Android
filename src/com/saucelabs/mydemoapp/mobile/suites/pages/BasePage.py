import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#
# Created By: Vasudevan Sampath
#
#  BasePage.py is a Base page class for all POM (Page Object Model) classes
# Has pytest fixture for setup and teardown of Appium driver

@pytest.mark.usefixtures("setup_teardown")
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_any_expected_condition(self, timeout_seconds = 15):
        return WebDriverWait(self.driver, timeout_seconds)

    def click(self, locator):
        self.wait_for_any_expected_condition(10).until(expected_conditions.presence_of_element_located(locator)).click()

    def set_text(self, locator, input_text):
        self.wait_for_any_expected_condition().until(expected_conditions.presence_of_element_located(locator)).send_keys(input_text)

    def get_text(self, locator):
        return self.wait_for_any_expected_condition().until(expected_conditions.visibility_of(locator)).get_attribute("innerText")

