from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox(executable_path="/home/pankaj/Documents/Drivers/geckodriver")
#will take us to the desired website
driver.get("http://newtours.demoaut.com")

driver.find_element_by_name("userName").send_keys('sharku002')
driver.find_element_by_name("password").send_keys('welcome@1234')
driver.find_element_by_name("login").click()

Passenger = Select(driver.find_element_by_name("passCount")).select_by_value("1")
DepartingFrom = Select(driver.find_element_by_name("fromPort")).select_by_value("London")
FromMonth = Select(driver.find_element_by_name("fromMonth")).select_by_value("5")
FromDy = Select(driver.find_element_by_name("fromDay")).select_by_value("1")
ToPort = Select(driver.find_element_by_name("toPort")).select_by_value("Portland")
ReturningMonth = Select(driver.find_element_by_name("fromMonth")).select_by_value("5")
ReturningDay = Select(driver.find_element_by_name("fromDay")).select_by_value("10")
serviceClass = driver.find_element_by_xpath("//input[@value='Business']").click()
airline = Select(driver.find_elements_by_name("airline")).select_by_visible_text("Unified Airlines")

#click on continue and we will be landed to pricing page for selecting the airline

