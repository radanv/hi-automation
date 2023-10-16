from Locators import *
from Elements import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "Master"

#base page (class) works as driver to test all pages
class BasePage():
    def __init__(self, driver):
        self.driver = driver

#main page will use basepage class for tests
class MainPage(BasePage):
    search_text_element = SearchTextElement()
    #check if the title of the main page is a Hosting Israel
    def is_title_matches(self):
        #return "Hosting Israel" is self.driver.title
        return "Hosting Israel" == self.driver.title
     
    def click_lang_button(self):
        element = self.driver.find_element(MainPageLocators.lang_button)
        element.click()

class ProductPage(BasePage):
    search_text_element = SearchTextElement()

class SearchResultPage(BasePage):
    def is_result_found(self):
        #return "Master wasn't found." not in self.driver.page_source
        return "Master was found." in self.driver.page_source
