from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox(executable_path="/home/pankaj/Documents/Drivers/geckodriver")
#will take us to the desired website
driver.get("http://newtours.demoaut.com")

#If no userId found Register your self
#the below code is for registration
driver.find_element_by_partial_link_text("Register").click()
driver.find_element_by_name("firstName").send_keys('Neel')
driver.find_element_by_name("lastName").send_keys("Desai")
driver.find_element_by_name("phone").send_keys("6666666666")
driver.find_element_by_name("userName").send_keys("nds@gmail.com")
driver.find_element_by_name("address1").send_keys("B/108, Villa Appartment")
driver.find_element_by_name("address2").send_keys("Near Bombay Street")
driver.find_element_by_name("city").send_keys("Pune")
driver.find_element_by_name("state").send_keys("Maharastra")
driver.find_element_by_name("postalCode").send_keys("000000")
#select country
obj = Select(driver.find_element_by_name("country"))
obj.select_by_value("92")

# will be my user name
driver.find_element_by_id("email").send_keys("sharku002")
driver.find_element_by_name("password").send_keys("welcome@1234")
driver.find_element_by_name("confirmPassword").send_keys("welcome@1234")
# handle dropdown

driver.find_element_by_name("register").click()

#time.sleep(5)
#driver.close()
