# getting the text data from the web page
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DemoGetTextData:
    def text_data(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.yatra.com/")
        text1 = driver.find_element(By.CSS_SELECTOR, "h1[class='paragraphHeading']").text
        print(text1)  # printing the text data
        driver.close()


# id = DemoGetTextData()
# id.text_data()


# getting the value of the attribute of html like name on button

class DemoGetAttributeValue:
    def attributs_value(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.yatra.com/")
        text1 = driver.find_element(By.XPATH,
                                    "//div[@class='ripple-parent search-height demo-icon icon-go']//input["
                                    "@id='BE_flight_flsearch_btn']").get_attribute('value')

        print(text1)  # printing attribute value
        driver.close()


av = DemoGetAttributeValue()
av.attributs_value()
