import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
"""
# driver = webdriver.Edge(executable_path="C://browserdrivers//msedgedriver.exe")
# we can use above line but code is executed with some error as DeprecationWarning to overcome we use service
driver = webdriver.Edge(service=Service(r"C://browserdrivers//msedgedriver.exe"))
driver.get("https://github.com/")
driver.maximize_window()
print(driver.title)
driver.close()
"""

# instead of downloading the browser exe file manually and accessing using path we can access by using webdriver-manager

# driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# as above to avoide deprecation warning we can use
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get("https://github.com/")
driver.maximize_window()
print(driver.title)
driver.close()
