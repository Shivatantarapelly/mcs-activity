import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class SearchFlightsResult(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def filter_flights(self):
        self.driver.find_element(By.XPATH, "//p[normalize-space()='1']").click()
        time.sleep(4)
        allstop = self.wait_for_presence_of_elements(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text("
                                                               "),'1 Stop') or contains(text(), '2 Stop')]")
        for stop in allstop:
            # print(stop.text)
            assert stop.text == "1 Stop"
            print("assert pass")
