import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Handling the mouse action by using ActionChain class to perform mouse operations


class HandleMouseHover:
    def mouse_hover(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(4)
        myaccount = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        # locating myaccount web element
        more = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        # loacating more web element
        achains = ActionChains(driver)
        # creating the object for the ActionChain class
        xplore = driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']")
        # locating the xplore button we we hoverover on more option
        achains.move_to_element(myaccount).perform()
        # moving the cursor to myaccount element
        time.sleep(4)
        achains.move_to_element(more).perform()
        # moving the cursor to more element
        # for clicking we can use achains.context_click(locator)
        # for double clicking we can use achains.double_click(locator)
        time.sleep(4)
        xplore.click()
        # clicking on xplore button
        time.sleep(4)


hm = HandleMouseHover()
hm.mouse_hover()
