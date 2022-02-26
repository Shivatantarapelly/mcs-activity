import time

import pytest
import softest as softest
from selenium.webdriver.common.by import By

from pages.search_flight_result_page import SearchFlightsResult
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils

"""
@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def test_search_flights(self):
        lp = LaunchPage(self.driver)
        sf = lp.search_flights("Bangalore", "Singapore", "30/04/2022")
        # lp.search flight will execute methods of launch page class and returns the object of search flight class
        # lp.enter_depart_place("Bangalore")
        # lp.enter_going_to_place("Singapore")
        # lp.enter_departure_date("30/04/2022")
        # lp.click_search_flight_button()
        lp.pagedown_scroll()
        # sf = SearchFlightsResult(self.driver)
        sf.filter_flights_by_stop("1 Stop")
        # allstop = self.wait_for_presence_of_elements(By.XPATH, "//span[contains(text(),'Non Stop') or contains(
        # text(),'1 Stop') or contains(text(), '2 Stops')]")
        allstop = sf.allstop_list()
        u = Utils()
        u.list_item_text(allstop, '1 Stop')
"""


# finally we the modified test case will be as below

@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.u = Utils()

    # 1st test case
    def test_search_flights_1_stop(self):
        sf = self.lp.search_flights("Bangalore", "Singapore", "30/04/2022")
        self.lp.pagedown_scroll()
        sf.filter_flights_by_stop("1 Stop")
        allstop = sf.allstop_list()
        self.u.list_item_text(allstop, '1 Stop')

    # 2nd test case
    def test_search_flights_non_stop(self):
        sf = self.lp.search_flights("Hyderabad", "Mumbai", "30/05/2022")
        self.lp.pagedown_scroll()
        sf.filter_flights_by_stop("Non Stop")
        allstop = sf.allstop_list()
        self.u.list_item_text(allstop, 'Non Stop')

# we can write multiple test cases by just refactoring
