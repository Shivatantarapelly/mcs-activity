import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class ExplicitFluent:
    def ef_wait(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.implicitly_wait(10)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        origincity = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        origincity.click()
        time.sleep(2)
        # origincity.clear() wait.until(EC.presence_of_element_located((By.XPATH, "//input[
        # @id='BE_flight_origin_city']"))).send_keys('Bangalore')
        origincity.send_keys("Bangalore")
        time.sleep(2)
        origincity.send_keys(Keys.ENTER)
        # Keys is a class by which we can handle all the keyboard buttons
        time.sleep(2)
        arrival = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        # arrival.send_keys('nan')
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']"))).send_keys('Nan')
        # time.sleep(2)
        goingto = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']"))).find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        # # in above the xpath should be changed from //div[@class='viewport'] to above by adding //div[1]/li
        # # which can get the list of suggestions which are in another div start from 1 and continues as list
        for place in goingto:
            if 'Nanded' in place.text:  # text gives the text data of the li tags
                # #         time.sleep(4)
                place.click()
                #         time.sleep(4)
                break
        # #
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        # time.sleep(4)
        datelist = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='month-wrapper']//tbody//td[@class!='inActiveTD weekend']"))).find_elements(
            By.XPATH, "//div[@class='month-wrapper']//tbody//td[@class!='inActiveTD weekend']")
        # # the above xpath is modified according to the data lies within html which should created manually.
        for date in datelist:
            if date.get_attribute("id") == "28/07/2022":
                driver.execute_script('arguments[0].click()', date)
                # as date.click() giving exception cannot click we can use above to perform click operation
                # time.sleep(4)
                break
        driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input["
                                      "@id='BE_flight_flsearch_btn']").click()
        time.sleep(5)


As = ExplicitFluent()
As.ef_wait()
