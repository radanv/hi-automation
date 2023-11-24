import pytest
from ..tests_stats.secure.creds import secureCreds
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Test_LoginPage:
    profile_page_url = "https://statistics.services.hosting-israel.co.il/client-registration-form.php"
    pageTitle = "Stats: Registration For Clients"
    loginOrRegisterText = "Log in or Sign up"
    notificationText = "Successful Login! The page will be reloaded in 3 seconds."
    userPhoneInput = "clientPhone"
    userPasswordInput = "clientPassword"
    formSubmitButtonName = "button"

    def test_Login(self, web_driver):
        #Check the page title
        self.driver.get(Test_LoginPage.profile_page_url)
        assert Test_LoginPage.pageTitle in self.driver.title
        #Check the current state notification text 
        stateNotificationText = self.driver.find_element(by=By.TAG_NAME, value="h4")
        assert stateNotificationText.text == Test_LoginPage.loginOrRegisterText
        time.sleep(3)
        #Find username/password fields and input credentials
        self.driver.find_element(By.NAME, Test_LoginPage.userPhoneInput).send_keys(secureCreds.username)
        self.driver.find_element(By.NAME, Test_LoginPage.userPasswordInput).send_keys(secureCreds.password)
        self.driver.find_element(By.CSS_SELECTOR, Test_LoginPage.formSubmitButtonName).click()
        #verify the notification text
        stateNotificationText = self.driver.find_element(by=By.TAG_NAME, value="h4")
        assert stateNotificationText.text == Test_LoginPage.notificationText

