from selenium import webdriver
import unittest
import Pages

class HostingIsraelMain(unittest.TestCase):                
        
        def setUp(self):
                #return super().setUp()
                self.driver = webdriver.Chrome()
                self.driver.get("http://hosting-israel.co.il/")

        def test_mainpage(self):
                mainPage = Pages.MainPage(self.driver)
                assert mainPage.is_title_matches()              #test if it's a main page
                mainPage.click_lang_button()                    #change the language to Eng

        def test_products(self):
                productPage = Pages.MainPage(self.driver)
                

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