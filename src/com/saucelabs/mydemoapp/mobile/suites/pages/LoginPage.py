from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions

from src.com.saucelabs.mydemoapp.mobile.suites.pages.BasePage import BasePage

#
# Created By: Vasudevan Sampath
#
#  LoginPage.py is a Login page class for all Login related methods
# Extends from BasePage class

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

# Locators
    bottom_menu_item_locator = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    login_menu_item_locator = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")
    username_locator = (AppiumBy.ACCESSIBILITY_ID, "bob@example.com-autofill")
    login_id_auto_fill_locator = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"bob@example.com\"]")
    login_button_locator = (AppiumBy.ACCESSIBILITY_ID, "Login button")
    logout_menu_item_locator = (AppiumBy.ACCESSIBILITY_ID, "Logout button")

# Login specific methods
    def navigate_to_login_page(self):
        self.click(self.bottom_menu_item_locator)
        self.click(self.login_menu_item_locator)

    def click_login_autofill(self):
        self.click(self.login_id_auto_fill_locator)

    def signin(self):
        self.click(self.login_button_locator)

    def do_login(self):
        self.navigate_to_login_page()
        self.click_login_autofill()
        self.signin()

    def is_login_successful(self):
        self.click(self.bottom_menu_item_locator)
        self.click(self.login_menu_item_locator)
        return self.wait_for_any_expected_condition().until(expected_conditions.invisibility_of_element(self.login_id_auto_fill_locator))



