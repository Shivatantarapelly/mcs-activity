import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def depart_from(self, departplace):
        departfrom = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_city']")
        departfrom.click()
        time.sleep(1)
        departfrom.send_keys(departplace)
        time.sleep(1)
        departfrom.send_keys(Keys.ENTER)

    def going_to(self, goingtoplace):
        arrival = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        arrival.click()
        time.sleep(1)
        arrival.send_keys(goingtoplace)
        time.sleep(1)
        searchresult = self.wait_for_presence_of_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        for place in searchresult:
            if goingtoplace in place.text:  # text gives the text data of the li tags
                place.click()
                break

    def select_date(self, date):
        self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
        datelist = self.wait_until_element_is_clickable(By.XPATH, "//div[@class='month-wrapper']//tbody//td["
                                                                  "@class!='inActiveTD weekend']").find_elements(
            By.XPATH, "//div[@class='month-wrapper']//tbody//td[@class!='inActiveTD weekend']")
        for dates in datelist:
            if dates.get_attribute("data-date") == date:
                self.driver.execute_script("arguments[0].click()", dates)
                break

    def clicksearch(self):
        self.driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input["
                                           "@id='BE_flight_flsearch_btn']").click()
        time.sleep(5)
