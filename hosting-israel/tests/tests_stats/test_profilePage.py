import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class Test_ProfilePage:
    profile_page_url = "https://statistics.services.hosting-israel.co.il/?phone=123456789"
    pageTitle = "Stats: Homepage"
    period_week = "week"
    period_month = "month"
    period_halfyear = "1/2year"
    period_year = "year"
    class_active = "active"

    def test_Title(self, web_driver):
        self.driver.get(Test_ProfilePage.profile_page_url)
        assert Test_ProfilePage.pageTitle in self.driver.title
        time.sleep(2)

    def test_PeriodWeek(self, web_driver):
        self.driver.get(Test_ProfilePage.profile_page_url)
        openPeriod = self.driver.find_element(By.NAME, Test_ProfilePage.period_week)
        openPeriod.click()
        #Check if the tab is active
        try:
            class_name = openPeriod.get_attribute("class")
            #print(class_name)
            assert Test_ProfilePage.class_active in class_name
        except NoSuchElementException as e:
            print(e)
        time.sleep(2)

    def test_PeriodMonth(self, web_driver):
        self.driver.get(Test_ProfilePage.profile_page_url)
        openPeriod = self.driver.find_element(By.NAME, Test_ProfilePage.period_month)
        openPeriod.click()
        #Check if the tab is active
        try:
            class_name = openPeriod.get_attribute("class")
            #print(class_name)
            assert Test_ProfilePage.class_active in class_name
        except NoSuchElementException as e:
            print(e)
        time.sleep(2)

    def test_Period6Month(self, web_driver):
        self.driver.get(Test_ProfilePage.profile_page_url)
        openPeriod = self.driver.find_element(By.NAME, Test_ProfilePage.period_halfyear)
        openPeriod.click()
        #Check if the tab is active
        try:
            class_name = openPeriod.get_attribute("class")
            #print(class_name)
            assert Test_ProfilePage.class_active in class_name
        except NoSuchElementException as e:
            print(e)
        time.sleep(2)

    def test_PeriodYear(self, web_driver):
        self.driver.get(Test_ProfilePage.profile_page_url)
        openPeriod = self.driver.find_element(By.NAME, Test_ProfilePage.period_year)
        openPeriod.click()
        #Check if the tab is active
        try:
            class_name = openPeriod.get_attribute("class")
            #print(class_name)
            assert Test_ProfilePage.class_active in class_name
        except NoSuchElementException as e:
            print(e)
        time.sleep(2)

    