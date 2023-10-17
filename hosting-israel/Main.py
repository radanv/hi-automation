from selenium import webdriver
import unittest
import Pages

class HostingIsraelMain(unittest.TestCase):                
        
        def setUp(self):
                #return super().setUp()
                options = webdriver.ChromeOptions()
                options.add_experimental_option("detach", True)             #disable auto quit
                self.driver=webdriver.Chrome(options=options)
                self.driver.get("http://hosting-israel.co.il/")
                self.driver.implicitly_wait(10)

        def test_mainpage(self):
                print("Main page")
                #Change language
                Language = Pages.LanguageButton(self.driver)    # change the language to English
                Language.click_lang_button()
                mainPage = Pages.MainPage(self.driver)
                assert mainPage.is_title_matches()              # test the title if it's a main page            

        def test_clients(self):
                print("Clients page")
                #Change language
                Language = Pages.LanguageButton(self.driver)    # change the language to English
                Language.click_lang_button()
                clientsPage = Pages.ClientsPage(self.driver)
                clientsPage.open_clients_page()

        #def test_searchText(self):
                #mainPage = Pages.MainPage(self.driver)
                #mainPage.search_text_element = "Hosting Israel"
                #search_result_page = Pages.SearchResultPage(self.driver)
                #assert search_result_page.is_result_found()

        def tearDown(self):
                return super().tearDown()
                #self.driver.close()

if __name__ == "__main__":
       unittest.main()               