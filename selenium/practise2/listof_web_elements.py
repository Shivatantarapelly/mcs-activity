import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DemoFindElementsList:
    def list_elements(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.yatra.com/")
        lista = driver.find_elements(By.TAG_NAME, "a")
        print(len(lista))  # find_elements gives the list of all elements with tag name 'a'
        time.sleep(6)


id = DemoFindElementsList()
id.list_elements()
