import pytest
from selenium import webdriver
  
@pytest.fixture(scope="function")
def web_driver(request):
    driver=webdriver.Chrome()
    #driver.get("https://statistics.services.hosting-israel.co.il/")
    request.instance.driver = driver
    driver.delete_all_cookies
    driver.implicitly_wait(10)

    yield
    driver.quit()
