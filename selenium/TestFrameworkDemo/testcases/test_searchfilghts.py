import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:
    def test_search_flights(self):
        origincity = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        origincity.click()
        time.sleep(2)
        origincity.send_keys("Bangalore")
        time.sleep(2)
        origincity.send_keys(Keys.ENTER)
        time.sleep(2)
        arrival = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']"))).send_keys('Hyd')

        goingto = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']"))).find_elements(By.XPATH,
                                                                                                           "//div[@class='viewport']//div[1]/li")

        for place in goingto:
            if 'Hyderabad' in place.text:  # text gives the text data of the li tags
                place.click()
                break
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        datelist = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='month-wrapper']//tbody//td[@class!='inActiveTD weekend']"))).find_elements(
            By.XPATH, "//div[@class='month-wrapper']//tbody//td[@class!='inActiveTD weekend']")
        for date in datelist:
            if date.get_attribute("id") == "28/07/2022":
                self.driver.execute_script('arguments[0].click()', date)
                break
        self.driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input["
                                      "@id='BE_flight_flsearch_btn']").click()
        time.sleep(5)


TSF = TestSearchAndVerifyFilter()
TSF.test_search_flights()
