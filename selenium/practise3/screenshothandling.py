import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# handling for taking screen shot of only web element and taking screen

class HandleScreenShot:
    def screenshot1(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        button = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        button.screenshot(".\\test1.png")   # this will take screen shot of only that web element
        button.click()
        time.sleep(4)
        driver.get_screenshot_as_file(".\\test2.png")
        driver.save_screenshot(".\\test2.png")  # here .//  . indicates that current working directory
        # we can use any of the above method for taking screen shots


Hs = HandleScreenShot()
Hs.screenshot1()