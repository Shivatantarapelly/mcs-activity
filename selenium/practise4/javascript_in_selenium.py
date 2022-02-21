import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# to execute javascript with selenium in order to find the complex web elements

class JSExecutionDemo:
    def jsdemo(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        # driver.get("https://www.rcvacademy.com/")
        driver.execute_script("window.open('https://www.rcvacademy.com/', '_self');")
        # in js we use above window.open() method to open any url and _self is to open in same tab not creating any tabs
        driver.maximize_window()
        time.sleep(4)
        jselement = driver.execute_script("return document.getElementsByTagName('a')[75];")
        # to execute script we use above method and passing script as parameter and return will give the web element
        # in browser by using console we can identify elements as document.get...so on give web element login
        driver.execute_script("arguments[0].click();", jselement)
        # by passing above argument we can perform click action on login element and we have give on which you have
        # to perform click action as we given jselement
        time.sleep(6)


js = JSExecutionDemo()
js.jsdemo()
