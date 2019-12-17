from selenium import webdriver
from sampledb import PanData
from selenium.webdriver.support.ui import Select


data = PanData()
datalistfirst = data.getPanDatai(0)
#print(datalistfirst.id)
driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
#driver.implicitly_wait(30)
#driver.maximize_window()
#driver.get("https://www.onlineservices.nsdl.com/paam/")
driver.get("http://localhost/NSDL/Login%20Manager.html")
alert_obj = driver.switch_to.alert
alert_obj.accept()
#Input field
#search_field = driver.find_element_by_id("search_form_input_homepage")

#Userid
#userfield = driver.find_element_by_id("userID")

areacode = driver.find_element_by_id("l_name")
areacode.send_keys("Hello")

pansubmit = driver.find_element_by_id("proceed")
#search_field.send_keys("Hello World")
#search_field.submit()
#driver.close()
