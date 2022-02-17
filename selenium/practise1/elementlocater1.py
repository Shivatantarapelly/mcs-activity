import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

"""
# Locating element by ID

class DemoFindElementsById:
    def locate_by_id(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.booking.com/index.html?aid=1535084&label=enin-edge-ntp-topsites-curate-ana")
        driver.find_elements(By.ID, "ss")
        # the above line is for finding the search box by id    
        action = ActionChains(driver)
        action.send_keys('hyderabad').perform()
        # the above line is for filling the search box with text data 'hyderabad' 
        time.sleep(6)


id = DemoFindElementsById()
id.locate_by_id()
"""

# Locating element by ID

"""
class DemoFindElementsByName:
    def locate_by_name(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.booking.com/index.html?aid=1535084&label=enin-edge-ntp-topsites-curate-ana")
        driver.find_elements(By.NAME, "ss")
        # the above line is for finding the search box by id
        action = ActionChains(driver)
        action.send_keys('hyderabad').perform()
        # the above line is for filling the search box with text data 'hyderabad'
        time.sleep(6)


id = DemoFindElementsByName()
id.locate_by_name()
"""


class DemoFindElementsByXPath:
    def locate_by_xpath(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.booking.com/index.html?aid=1535084&label=enin-edge-ntp-topsites-curate-ana")
        driver.find_elements(By.XPATH, "//input[@id='ss']")
        # the above line is for finding the search box by id
        action = ActionChains(driver)
        action.send_keys('hyderabad').perform()
        # the above line is for filling the search box with text data 'hyderabad'
        time.sleep(6)


id = DemoFindElementsByXPath()
id.locate_by_xpath()
