from appium import webdriver

import unittest
#Infromacion del dispositivo y app en uso
#C:\Users\fabra>adb shell "dumpsys activity activities | grep mResumedActivity"
from selenium.webdriver.common.by import By

driver = {
    "platformName": "Android",
    "appium:platformVersion": "12",
    "appium:deviceName": "crosshatch",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.google.android.youtube",
    "appium:appActivity": "com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity",
    "appium:newCommandTimeout":"3600"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Expandir reproductor en miniatura"]/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup')\
      .click

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
