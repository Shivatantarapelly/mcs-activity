
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class ImplicitWait:
    def implicit(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.implicitly_wait(10)
        # this will see that if web element is present then perform action and continues or if web element is not
        # present then it pauses and checks for 10secs untill it load and then continues after timeout
        driver.get("https://login.salesforce.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys('shiva prasad')
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys('123456')


iw = ImplicitWait()
iw.implicit()
