import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# to know whether the element state is enable or disabled

class ElementState:
    def state(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://accounts.pega.com/register")
        state = driver.find_element(By.XPATH, "//button[@id='edit-submit']").is_enabled()
        print(state)  # here the state is disabled as the details should be entered
        driver.find_element(By.XPATH, "//input[@id='edit-first-name-0-value']").send_keys('sai')
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='edit-last-name-0-value']").send_keys('prasad')
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='edit-employer-0-value']").send_keys('xyz')
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='edit-mail-0-value']").send_keys('xyz@gmail.com')
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='edit-pass']").send_keys('Xyz@2020')
        state1 = driver.find_element(By.XPATH, "//button[@id='edit-submit']").is_enabled()
        print(state1)  # here the state is enable the data is entered


s = ElementState()
s.state()
