from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/pankaj/Documents/Drivers/geckodriver")
driver.get("http://newtours.demoaut.com")

#can be saved in any extension
driver.save_screenshot("/home/pankaj/FisTask/booking.jpg")

#can be saved in only png
driver.get_screenshot_as_file("/home/pankaj/FisTask/sample1.png")