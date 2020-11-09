#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 16:04
'''

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasicPage():
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:62001"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "True"
            caps["skipDeviceInitialization"] = "True"
            caps["skipServerInstallation"] = "True"
            # caps["dontStopAppOnReset"] = "True"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(8)
        else:
            self.driver = driver

    def findAndClick(self, by, locator):
        return self.driver.find_element(by, locator).click()

    def findAndSendKeys(self, by, locator, value):
        return self.driver.find_element(by, locator).send_keys(value)

    def getPageSource(self):
        return self.driver.page_source

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def waitElementPresent(self, by, locator):
        return WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_all_elements_located((by, locator)))

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        from app.Pages.main_page import MainPage
        return MainPage(self.driver)
