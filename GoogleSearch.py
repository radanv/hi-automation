from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Chrome browser configuration
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)             #disable auto quit
driver=webdriver.Chrome(options=options)
driver.get("https://google.com")

#get the page title
title = driver.title
assert title == "Google"

print("Open the website")
driver.implicitly_wait(10)
#Find "Search" field on the website
search_textarea = driver.find_element(by=By.XPATH, value="//textarea[@type='search']")
print("The Search area was found")

#Search for "selenium library"
search_textarea.send_keys("selenium library")               #enter selenium library
print("The search area was filled")
search_textarea.send_keys(Keys.ENTER)                       #click enter button to confirm the search            
print("Enter button was pressed")

#parse the page to find the link
try:
    #Get links from articles
    search_links = driver.find_elements(by=By.XPATH, value="//a[@href and .//h3[text()='Install a Selenium library']]")

    if (search_links):
        print("Links were found")
        #Get all links from the page
        for l in search_links:
            print(l.get_attribute("href"))

        #Navigate to the article "Install a Selenium library"
        selenium_page = driver.find_element(by=By.XPATH, value="//*[text()='Install a Selenium library']")
        selenium_page.click()

        #Select language tab Python
        language_tab = driver.find_element(by=By.CLASS_NAME, value="persistLang-Python")
        language_tab.click()
        print("done")
        driver.back()

    else:
        print("Links were not found")
    
finally:
    driver.quit()