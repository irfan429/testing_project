from selenium import webdriver
import time


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_Username(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        # time.sleep(10)
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def set_Password(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        # time.sleep(10)
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_Login(self):
        # time.sleep(5)
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_Logout(self):
        self.driver.find_element_by_xpath(self.link_logout_linktext).click()

