import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.select import Select


# for handling the drop down list to select single data which is created using select tag in html
# the drop down list which is created by not using select tag can throw the exception

class HandleSingleDropDown:
    def sdropdown(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.salesforce.com/uk/form/signup/freetrial-sales-pe/")
        driver.maximize_window()
        drpdwn = driver.find_element(By.NAME, "CompanyEmployees")
        dd = Select(drpdwn)
        dd.select_by_index(1)
        time.sleep(4)
        dd.select_by_value('150')
        time.sleep(4)
        dd.select_by_visible_text('200 - 749 employees')
        time.sleep(4)


# sdd = HandleSingleDropDown()
# sdd.sdropdown()

# handling dropdown list by selecting multiple data and also deselecting the data
# multi select can also be done by using select_by_value, select_by_index, select_by_visible_text
# we can deselect by using the same deselect_by_value, deselect_by_index, deselect_by_visible_text
