from Locators import *
from Elements import BasePageElement

#Search page is not available now
#class SearchTextElement(BasePageElement):
    #locator = "Master"

#base page (class) works as driver to test all pages
class BasePage():
    def __init__(self, driver):
        self.driver = driver

#main page will use basepage class for tests
class MainPage(BasePage):

    #check if the title of the main page is a Hosting Israel
    def is_title_matches(self):
        #return "Hosting Israel" is self.driver.title
        return "Hosting Israel" == self.driver.title

class ClientsPage(BasePage):
    def open_clients_page(self):
        openClientsPage = self.driver.find_element(*Main_Menu.clients_button)
        openClientsPage.click()

#Search page is not available now
#class SearchPage(BasePage):
    #search_text_element = SearchTextElement()

#Search page is not available now
#class SearchResultPage(BasePage):
    #def is_result_found(self):
        #return "Master wasn't found." not in self.driver.page_source
        #return "Master was found." in self.driver.page_source

class LanguageButton(BasePage):
    def click_lang_button(self):
        changeLangToEng = self.driver.find_element(*Main_Menu.eng_button)
        changeLangToEng.click()
