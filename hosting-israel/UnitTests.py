from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_eight_components():

    #Chrome browser configuration
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(options=options)
    
    #start page
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    #get the page title
    title = driver.title
    assert title == "Web form"
    #wait for it
    driver.implicitly_wait(1.5)

    #variables
    text_input = driver.find_element(by=By.NAME, value="my-text")
    password = driver.find_element(by=By.NAME, value="my-password")
    textarea = driver.find_element(by=By.NAME, value="my-textarea")
    disabled_input = driver.find_element(by=By.XPATH, value="//input[@placeholder='Disabled input']")
    dropdown = driver.find_element(by=By.NAME, value="my-select")
    default_checkbox = driver.find_element(by=By.ID, value="my-check-2")
    color = driver.find_element(by=By.NAME, value="my-colors")
    date_picker = driver.find_element(by=By.NAME, value="my-date")
    empty_click = driver.findElement(by=By.XPATH, value="//html")
    #submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    #tests
    text_input.send_keys("Selenium")
    password.send_keys("12345678")
    textarea.send_keys("Lorem ipsum, Lorem ipsum, Lorem ipsum")

    assert disabled_input.is_enabled

    dropdown.click()
    select = Select(dropdown)
    select.select_by_value('3')
    dropdown.click()
    default_checkbox.click()
    color.clear
    color.send_keys("#FFFFFF")
    date_picker.click()
    date_picker.send_keys("10102023")
    empty_click.click()
    #submit_button.click()

    #message = driver.find_element(by=By.ID, value="message")
    #value = message.text
    #assert value == "Received!"
    #driver.quit()

test_eight_components()