import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager



# in a window we can have multiple frame which are created by using iframes tags. the elements which fall inside
# can be accessed only after switching to that frame

class HandleIFrames:
    def iframes(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.w3schools.com/html/html_iframe.asp")
        driver.maximize_window()
        time.sleep(4)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='W3Schools HTML Tutorial']"))
        # we can switch to frame by passing iframe path as xpath
        driver.find_element(By.ID, "w3loginbtn").click()
        time.sleep(4)


fr = HandleIFrames()
fr.iframes()
