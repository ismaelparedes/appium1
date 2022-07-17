from appium import webdriver
from select import select
from selenium.webdriver.common.by import By
#Infromacion del dispositivo y app en uso
#C:\Users\fabra>adb shell "dumpsys activity activities | grep mResumedActivity"
driver ={
  "platformName": "Android",
  "platformVersion": "12",
  "deviceName": "crosshatch",
  "automationName": "UiAutomator2",
  "appPackage": "com.google.android.calculator",
  "appActivity": "com.android.calculator2.Calculator"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

#suma de dos numero
#Click para abrir
driver.find_element(By.ID,'com.google.android.calculator:id/collapse_expand').click()
#Click para cerrar
driver.find_element(By.ID,'com.google.android.calculator:id/collapse_expand').click()

driver.find_element(By.ID,'com.google.android.calculator:id/digit_9').click()
driver.find_element(By.ID,'com.google.android.calculator:id/op_add').click()
driver.find_element(By.ID,'com.google.android.calculator:id/digit_8').click()
driver.find_element(By.ID,'com.google.android.calculator:id/eq').click()

#valor = select(driver.find_element(By.ID,'com.google.android.calculator:id/formula')).