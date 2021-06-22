import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customlogger import LogGeneration


class Test_001_Login:
    baseURL = Readconfig.get_url()
    username = Readconfig.get_username()
    password = Readconfig.get_password()
    logger = LogGeneration.loggen()

    def test_home_page_title(self, setup):
        self.logger.info("********** Test_001_Login ***************")
        self.logger.info("********** Verifying Home Page ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()

        if act_title == "Your store. Login":
            assert True
            # self.driver.close()
            self.logger.info("********** Home Page title test is passed ***************")
        else:
            # assert False
            self.driver.save_screenshot("test_home_page_title_screenshot.png")
            self.driver.close()
            self.logger.warn("********** Home page test case is failed  ***************")
            assert False
        # return self.get_screenshot_As_file("Screenshots.png")

    def test_login(self, setup):
        self.logger.info("********** Verifying Login test  ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_Username(self.username)
        self.lp.set_Password(self.password)
        self.lp.click_Login()
        title = self.driver.title
        # print(title)
        self.driver.close()
        if title == "Dashboard / nopCommerce administration":
            # self.driver.save_screenshot("test_login.png")
            assert True
        else:
            # assert False
            time.sleep(20)
            self.driver.save_screenshot("test_login.png")
            self.driver.close()
            assert False
        # return self.get_screenshot_As_file("Screenshots.png")



