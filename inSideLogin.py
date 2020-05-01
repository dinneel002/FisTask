from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox(executable_path="/home/pankaj/Documents/Drivers/geckodriver")
#will take us to the desired website
driver.get("http://newtours.demoaut.com")
time.sleep(3)
driver.find_element_by_xpath("//*[text()='SIGN-ON']").click()
driver.find_element_by_name("userName").send_keys('sharku002')
driver.find_element_by_name("password").send_keys('welcome@1234')
driver.find_element_by_name("login").click()

#time.sleep(10)

time.sleep(60)
check_login = driver.find_element_by_xpath("//img[@src = '/images/masts/mast_flightfinder.gif']")
if (check_login == True):
    print("Login...")
else:
    print("no login happened")
obj = Select(driver.find_element_by_xpath("//select[@name='passCount']"))
obj.select_by_value("2")
print(Passenger)
