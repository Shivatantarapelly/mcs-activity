import time

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def setup(request):
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


# the below is for using multiple search engine using cmd
"""
@pytest.fixture(scope="class", autouse=True)
def setup(request, browser, url):
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get(url)
    # driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def url(request):
    return request.config.getoption("--url")
"""
