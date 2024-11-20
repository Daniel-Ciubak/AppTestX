import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.devtools.v127.fed_cm import click_dialog_button
from unittest import IsolatedAsyncioTestCase



class chop(unittest.TestCase):

    def createDriver(self):
        options = UiAutomator2Options()
        options.platform_version = "Android"
        options.automation_name = "UiAutomator2"
        options.platform_version = "12"
        options.device_name = "emulator-5554"
        options.app_package = "com.xy.xyz"
        options.app_activity = "com.xy.xyz.startup.StartupActivity"
        appium_server_url = "http://127.0.0.1:4723"
        driver = webdriver.Remote(appium_server_url, options=options)

        return driver






    def test_alanguage(self):
        driver = self.createDriver()
        t_language = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.xy.xyz:id/marketName" and @text="United States/English"]')
        self.assertTrue(t_language.is_displayed(), "Button not found")
        t_language.click()
        time.sleep(30)

        cookies=driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.xy.xyz:id/btn_accept_cookies"]')
        self.assertTrue(cookies.is_displayed(), "Button not found")
        cookies.click()
        time.sleep(30)

        consents=driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="android:id/button1"]')
        self.assertTrue(consents.is_displayed(), "Button not found")
        consents.click()
        time.sleep(30)

        bag=driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Your shopping bag"]')
        bag.click()
        time.sleep(20)
        driver.swipe(540, 1516, 522, 1186, 400)
        time.sleep(10)
        heart=driver.find_element(AppiumBy.XPATH,value='(//android.view.View[@content-desc="Favourite Inactive"])[1]')
        heart.click()
        time.sleep(10)
        back=driver.find_element(AppiumBy.XPATH,value='//android.widget.ImageButton[@content-desc="Back"]')
        back.click()
        time.sleep(10)
        heard=driver.find_element(AppiumBy.XPATH,value='//android.widget.Button[@content-desc="My Favorites"]')
        heard.click()
        time.sleep(10)
        loupe=driver.find_element(AppiumBy.XPATH,value='//android.view.View[@content-desc="Menu"]')
        for z in range(1,11):
            loupe.click()
        time.sleep(10)
        text_filed = driver.find_element(AppiumBy.XPATH, value='//android.widget.TextView[@text="Search"]')
        text_filed.send_keys("asia have cat")
        time.sleep(10)
        find_text = driver.find_element(AppiumBy.XPATH, value='//android.widget.TextView')
        compare_text = find_text.text
        self.assertEqual(compare_text, "asia have cat")
        driver.background_app(10)

        compare_text = find_text.text
        self.assertEqual(compare_text, "asia have cat")

        pass


if __name__ == '__main__':
    unittest.main()