from selenium import webdriver

driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
#driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://www.onlineservices.nsdl.com/paam/")
#driver.get("http://localhost/Pan/admin/mainprofile.php?")

#Input field
#search_field = driver.find_element_by_id("search_form_input_homepage")

#Userid
userfield = driver.find_element_by_id("userID")


search_field.send_keys("Hello World")
#search_field.submit()

