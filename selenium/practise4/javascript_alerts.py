import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.alert import Alert


# In windows there are some cases were we need to interact with javascript alert box also.In windows
# there are some cases were we need to interact with javascript alert box also. using some alert method we
# can access or also by importing Alert class from selenium.webdriver.common.alert import Alert

class JSAlerts:
    def popups(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        time.sleep(4)
        driver.switch_to.frame("iframeResult")
        # switching the iframe with iframe id
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(4)
        # # accepting the alert
        # driver.switch_to.alert.accept()
        # time.sleep(4)

        # get the text data of alert box
        print(driver.switch_to.alert.text)

        # # cancelling the alert
        # driver.switch_to.alert.dismiss()
        # time.sleep(4)

        # sending data into the alertbox
        driver.switch_to.alert.send_keys('shiva prasad')
        time.sleep(4)
        driver.switch_to.alert.accept()
        time.sleep(4)


jsa = JSAlerts()
jsa.popups()
