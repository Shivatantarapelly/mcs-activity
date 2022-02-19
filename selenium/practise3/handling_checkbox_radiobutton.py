import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# for handling the check boxes and radio buttons

class HandleCheckBoxes:
    def checkbox(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        time.sleep(4)
        print(driver.find_element(By.ID, "interest_market_c0").is_selected())  # here it is false
        driver.find_element(By.ID, "interest_market_c0").click()
        time.sleep(4)
        print(driver.find_element(By.ID, "interest_market_c0").is_selected())  # here it returns true
        driver.find_element(By.ID, "interest_sell_c0").click()
        time.sleep(4)
        driver.find_element(By.ID, "interest_serve_c0").click()
        time.sleep(4)


# cb = HandleCheckBoxes()
# cb.checkbox()


class RadioButton:
    def button(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        time.sleep(4)
        print(driver.find_element(By.ID, "doi0").is_selected())  # here it is false
        driver.find_element(By.ID, "doi0").click()
        time.sleep(4)
        print(driver.find_element(By.ID, "doi0").is_selected())  # here it returns true
        driver.find_element(By.ID, "doi1").click()
        time.sleep(4)
        print(driver.find_element(By.ID, "doi0").is_selected())  # here it returns false
        print(driver.find_element(By.ID, "doi1").is_selected())  # here it returns true


rb = RadioButton()
rb.button()
