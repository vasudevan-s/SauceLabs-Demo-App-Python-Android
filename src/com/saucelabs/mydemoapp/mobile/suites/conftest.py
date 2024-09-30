from appium import webdriver
from appium.options.android import UiAutomator2Options

import pytest

from src.com.saucelabs.mydemoapp.mobile.misc.Common import Common

#
# Created By: Vasudevan Sampath
#
#  Python file for setup and teardown actions

@pytest.yield_fixture()
def setup_teardown(request):
    common = Common()
    udid = common.read_device_config("devices", "udid")
    platformname = common.read_device_config("devices", "platformname")
    devicename = common.read_device_config("devices", "devicename")
    platformversion = common.read_device_config("devices", "platformVersion")
    automationname = common.read_device_config("devices", "automationName")
    packagename = common.read_device_config("devices", "packageName")
    activityname = common.read_device_config("devices", "activityName")
    caps = {
        "udid": udid,
        "deviceName": devicename,
        "platformName": platformname,
        "platformVersion": platformversion,
        "automationName": automationname,
        "appPackage": packagename,
        "appActivity": activityname,
    }
    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote("http://localhost:4723", options=options)
    request.cls.driver = driver
    yield
    if driver is not None:
        driver.quit()



