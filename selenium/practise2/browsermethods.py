import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# driver.get('url')
# driver.current_url
# driver.back()
# driver.forward()
# driver.refresh()
# driver.title
# driver.maximize_window()
# driver.minimize_window()
# driver.fullscreen_window()
# driver.close()
# driver.quit()


class DemoBrowserCommands:
    def commands(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.yatra.com/")  # to open url
        print(driver.current_url)  # to get the current url which is opened
        print(driver.title)  # to get the title of the web page
        driver.maximize_window()
        time.sleep(3)
        driver.fullscreen_window()
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[@class='demo-icon icon-hotels']").click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        driver.minimize_window()
        time.sleep(3)
        # driver.close()  # close the current window
        driver.quit()  # close all windows of that driver session


bc = DemoBrowserCommands()
bc.commands()
