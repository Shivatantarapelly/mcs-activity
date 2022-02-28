import logging
import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.utils import Utils


class SearchFlightsResult(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FILTER_BY_1_STOP_ICON = "//p[normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[normalize-space()='0']"
    ALL_STOPS_LIST = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(), '2 Stops')]"

    def get_filter_by_one_stop_icon(self):
        self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON).click()

    def get_filter_by_two_stop_icon(self):
        self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON).click()

    def get_filter_by_non_stop_icon(self):
        self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON).click()

    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon()
            self.log.warning("selected flights with 1 stop")
            time.sleep(2)
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon()
            self.log.warning("selected flights with 2 stop")
            time.sleep(2)
        if by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon()
            self.log.warning("selected flights with Non stop")
            time.sleep(2)
        else:
            self.log.warning("please provide valid filter stop")

    def allstop_list(self):
        return self.wait_for_presence_of_elements(By.XPATH, self.ALL_STOPS_LIST)
