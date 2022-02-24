import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request):
    print("initiating Edge......")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()
