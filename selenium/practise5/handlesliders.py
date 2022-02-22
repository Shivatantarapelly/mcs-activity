import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# handling slider like price between which is seen while shopping. this slider can handle by various methods of
# Action class


class HandleSlider:
    def slider(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.snapdeal.com/products/electronics-earphones?sort=plrty")
        driver.maximize_window()
        time.sleep(4)
        lslide = driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
        rslide = driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")
        achains = ActionChains(driver)
        achains.drag_and_drop_by_offset(lslide, 40, 0).perform()
        # the above method is to slide from left point to right where 60 is pixel on x axis and 0 as y axis not exists
        time.sleep(4)
        # achains.move_to_element(lslide).pause(1).click_and_hold(lslide).move_by_offset(60, 0).release().perform()
        # achains.click_and_hold(lslide).pause(1).move_by_offset(50, 0).release().perform()
        # the above is another two way of handling the slider
        achains.drag_and_drop_by_offset(rslide, -50, 0).perform()
        # the above method is to slide from right point to left where -60 is pixel on x axis and backward direction
        time.sleep(5)


hs = HandleSlider()
hs.slider()
