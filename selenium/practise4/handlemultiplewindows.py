import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# to handle multiple windows by switching the control from one window to another

class HandleMultiWindow:
    def multiwindow(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(4)
        window1 = driver.current_window_handle
        # the above will give the current window handle
        driver.find_element(By.XPATH, "//a[@title='Kerala Tourism Winter Holidays Campaign']//img[@class='conta iner "
                                      "large-banner']").click()
        # the above will click on webelement which opens another site in new window
        time.sleep(4)
        windowsls = driver.window_handles
        # gives list of handles of window till now opened
        for window in windowsls:
            if window != window1:
                driver.switch_to.window(window)
                # switching handle from first to second window
                window2 = driver.current_window_handle
                driver.find_element(By.XPATH, "//img[@title='Get it on Google Play']").click()
                # clicking on another web element to open another site in new window
                time.sleep(4)
                driver.close()
                # closing that current window i.e second window
                time.sleep(2)
                break
        windowls1 = driver.window_handles
        # now will give list of handles of present two windows
        for win in windowls1:
            if win != window1:
                driver.switch_to.window(win)
                driver.find_element(By.XPATH, "//input[@id='gbqfq']").send_keys('telangana tourism app')
                time.sleep(4)
                driver.find_element(By.XPATH, "//span[@class='gbqfi gb_uc']").click()
                time.sleep(4)
                driver.close()
                time.sleep(2)
                break
        driver.switch_to.window(window1)
        # finally switching to the parent window
        driver.find_element(By.XPATH, "//a[@title='Kerala Tourism Winter Holidays Campaign']//img[@class='conta iner "
                                      "large-banner']").click()
        time.sleep(4)
        driver.quit()


mw = HandleMultiWindow()
mw.multiwindow()
