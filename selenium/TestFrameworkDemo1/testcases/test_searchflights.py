import time

import pytest
from selenium.webdriver.common.by import By

from pages.search_flight_result_page import SearchFlightsResult
from pages.yatra_launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def test_search_flights(self):
        lp = LaunchPage(self.driver)
        lp.depart_from("Bangalore")
        lp.going_to("Singapore")
        lp.select_date("25/03/2022")
        lp.clicksearch()
        lp.pagedown_scroll()
        sf = SearchFlightsResult(self.driver)
        sf.filter_flights()





