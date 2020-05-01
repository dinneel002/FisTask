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

time.sleep(15)
check_login = driver.find_element_by_xpath("//img[@src = '/images/masts/mast_flightfinder.gif']")
if (check_login == True):
    print("Login...")
else:
    print("no login happened")

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

Depart = Select(driver.find_elements_by_name("outFlight")).select_by_value("Pangea Airlines$362$274$9:17")
Return = Select(driver.find_elements_by_name("inFlight")).select_by_value("Blue Skies Airlines$630$270$12:23")

driver.find_element_by_name("reserveFlights").click()

# card details
driver.find_element_by_name("passFirst0").send_keys("Neel")
driver.find_element_by_name("passLast0").send_keys("Desai")
driver.find_element_by_name("creditnumber").send_keys("9876787654567895")

#click on Secure Purchase
driver.find_element_by_name("buyFlights").click()

time.sleep(3)

#take screenshot of the booking

driver.save_screenshot("/home/pankaj/FisTask/booking.jpg")