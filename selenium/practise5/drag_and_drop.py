import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class HandleDragDrop:
    def dragdrop(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(4)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        source = driver.find_element(By.XPATH, "//p[normalize-space()='Drag me to my target']")
        target = driver.find_element(By.XPATH, "//div[@id='droppable']")
        ActionChains(driver).drag_and_drop(source, target).perform()
        # here source is the element we want to drag and drop and target is the location
        # ActionChains(driver).drag_and_drop_by_offset(source, 40, 50)
        # we can use above but according to x and y axis coordinates the source will move
        time.sleep(5)


dd = HandleDragDrop()
dd.dragdrop()
