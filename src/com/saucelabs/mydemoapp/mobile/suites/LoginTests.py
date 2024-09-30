import pytest

from src.com.saucelabs.mydemoapp.mobile.suites.pages.LoginPage import LoginPage

#
# Created By: Vasudevan Sampath
#
#  TestLogin.py is a Login test class for all Login related actions

@pytest.mark.usefixtures("setup_teardown")
class TestLogin:

    def test_verify_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.do_login()
        assert login_page.is_login_successful() == True