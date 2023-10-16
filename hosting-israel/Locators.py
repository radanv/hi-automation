from selenium.webdriver.common.by import By

class Main_Menu(object):
    eng_button = (By.LINK_TEXT, "English")
    heb_button = (By.LINK_TEXT, "ראשי")
    home_button = (By.LINK_TEXT, "Home")
    about_button = (By.LINK_TEXT, "About")
    products_button = (By.LINK_TEXT, "Products")
    clients_button = (By.LINK_TEXT, "Clients")
    contact_button = (By.LINK_TEXT, "Contact")

#Not active class
class MainPageLocators(object):
    home_page_option1 = ()

#Clients page locators are here
class ClientsPageLocators(object):
    clients_page_option1 = ()
    
#Search page is not available now
##class SearchResultsPageLocators(object):
   #pass