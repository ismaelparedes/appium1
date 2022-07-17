from appium import webdriver

import unittest
#Infromacion del dispositivo y app en uso
#C:\Users\fabra>adb shell "dumpsys activity activities | grep mResumedActivity"
driver = {
    "platformName": "Android",
    "appium:platformVersion": "12",
    "appium:deviceName": "crosshatch",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.google.android.calculator",
    "appium:appActivity": "com.android.calculator2.Calculator"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
