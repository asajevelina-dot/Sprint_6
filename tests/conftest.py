import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("useAutomationExtension", False)
    
    service = Service(r"C:\Users\User\Desktop\Sprint_6\geckodriver.exe")
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.maximize_window()
    
    yield driver
    driver.quit()