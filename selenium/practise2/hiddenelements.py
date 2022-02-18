import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# to know hidden elements are displayed are not. if the element exist in dom i.e html code it will give true
#  or false if element is in displayed state or not. if element not present in dom then it will throw exception

# the below class is to check the element is displayed or not in case of it is present in dom

class HiddenElementState:
    def state(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        res = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(res)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        res1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(res1)


# e = HiddenElementState()
# e.state()

# the below class is to check the element is displayed or not in case of it is not present in dom

class HiddenDestroyedElementState:
    def state1(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.yatra.com/hotels")
        time.sleep(4)
        driver.find_element(By.XPATH, "//i[@class='icon icon-angle-right arrowpassengerBox']").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div["
                                      "1]//span[2]").click()
        time.sleep(4)
        res = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(res)
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div["
                                      "1]//span[1]").click()
        time.sleep(4)
        res1 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        # the above line throws exception as the element not exist in dom
        print(res1)


h = HiddenDestroyedElementState()
h.state1()
