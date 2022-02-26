import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from pages.search_flight_result_page import SearchFlightsResult


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOINGTO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOINGTO_PLACES_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES_LIST = "//div[@class='month-wrapper']//tbody//td[@class!='inActiveTD weekend']"
    FLIGHT_SEARCH_BUTTON = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[" \
                           "@id='BE_flight_flsearch_btn'] "

    def get_depart_from_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def get_going_to_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOINGTO_FIELD)

    def get_going_to_places_list(self):
        return self.wait_for_presence_of_elements(By.XPATH, self.GOINGTO_PLACES_LIST)

    def get_date_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def get_date_field_list(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES_LIST)

    def get_search_button(self):
        return self.driver.find_element(By.XPATH, self.FLIGHT_SEARCH_BUTTON)

    def enter_depart_place(self, departplace):
        self.get_depart_from_field().click()
        time.sleep(1)
        self.get_depart_from_field().send_keys(departplace)
        time.sleep(1)
        self.get_depart_from_field().send_keys(Keys.ENTER)

    # def depart_from(self, departplace):
    #     departfrom = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_city']")
    #     departfrom.click()
    #     time.sleep(1)
    #     departfrom.send_keys(departplace)
    #     time.sleep(1)
    #     departfrom.send_keys(Keys.ENTER)

    def enter_going_to_place(self, goingto):
        self.get_going_to_field().click()
        time.sleep(1)
        self.get_going_to_field().send_keys(goingto)
        time.sleep(1)
        search_result = self.get_going_to_places_list()
        for place in search_result:
            if goingto in place.text:
                place.click()
                break

    # def going_to(self, goingtoplace):
    #     arrival = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_arrival_city']")
    #     arrival.click()
    #     time.sleep(1)
    #     arrival.send_keys(goingtoplace)
    #     time.sleep(1)
    #     searchresult = self.wait_for_presence_of_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
    #     for place in searchresult:
    #         if goingtoplace in place.text:  # text gives the text data of the li tags
    #             place.click()
    #             break

    def enter_departure_date(self, depart_date):
        self.get_date_field().click()
        datelist = self.get_date_field_list().find_elements(By.XPATH, self.ALL_DATES_LIST)
        for date in datelist:
            if date.get_attribute("data-date") == depart_date:
                self.driver.execute_script("arguments[0].click()", date)
                break

    # def select_date(self, date):
    #     self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
    #     datelist = self.wait_until_element_is_clickable(By.XPATH, "//div[@class='month-wrapper']//tbody//td[@class!='inActiveTD weekend']").find_elements(By.XPATH, "//div[@class='month-wrapper']//tbody//td[@class!='inActiveTD weekend']")
    #     for dates in datelist:
    #         if dates.get_attribute("data-date") == date:
    #             self.driver.execute_script("arguments[0].click()", dates)
    #             break

    def click_search_flight_button(self):
        self.get_search_button().click()
        time.sleep(5)

    # def clicksearch(self):
    #     self.driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
    #     time.sleep(5)

    def search_flights(self, departplace, goingto, departdate):
        self.enter_depart_place(departplace)
        self.enter_going_to_place(goingto)
        self.enter_departure_date(departdate)
        self.click_search_flight_button()
        search_flight = SearchFlightsResult(self.driver)
        return search_flight