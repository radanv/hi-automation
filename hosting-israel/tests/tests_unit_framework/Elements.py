from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_elements(by=By.NAME, value=self.locator))
        driver.find_elements(by=By.NAME, value=self.locator).clear()
        driver.find_elements(by=By.NAME, value=self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_elements(by=By.NAME, value=self.locator))
        element = driver.find_elements(by=By.NAME, value=self.locator)
        return element.get_attribute("value")