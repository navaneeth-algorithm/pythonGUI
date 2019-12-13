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
driver.get("http://localhost/Pan/admin/mainprofile.php?")
#alert_obj = driver.switch_to.alert
#alert_obj.accept()
#Input field
#search_field = driver.find_element_by_id("search_form_input_homepage")

#Userid
#userfield = driver.find_element_by_id("userID")

areacode = driver.find_element_by_id("areacode")
areacode.send_keys(datalistfirst.areacode)

aotype = driver.find_element_by_id("aotype")
aotype.send_keys(datalistfirst.assessingofficertype)

aonumber = driver.find_element_by_id("aonumber")
aonumber.send_keys(datalistfirst.assessingtypeofficernumber)

rangecode = driver.find_element_by_id("rangecode")
rangecode.send_keys(datalistfirst.rangecode)

applicanttitle = Select(driver.find_element_by_id("applicanttitle"))
applicanttitle.select_by_value(str(datalistfirst.titleid))

applicantlastname = driver.find_element_by_id("applicantlastname")
applicantlastname.send_keys(datalistfirst.lastname)

#driver.implicitly_wait(5)
applicantfirstname = driver.find_element_by_id("applicantfirstname")
print(datalistfirst.firstname)
#firstname.click()
#Element not intercatable ERRORR
applicantfirstname.send_keys(datalistfirst.firstname)

applicantmiddlename = driver.find_element_by_id("applicantmiddlename")
applicantmiddlename.send_keys(datalistfirst.middlename)

panname = driver.find_element_by_id("panname")
panname.send_keys(datalistfirst.panname)


#othernameflagyes = driver.find_element_by_id("othernameflagyes")

#othernameflagno = driver.find_element_by_id("othernameflagno")
if datalistfirst.aliastitleid!=0:
    radioElement = driver.find_element_by_id("othernameflagyes")
    radioElement.click()
    aliasapplicanttitle = Select(driver.find_element_by_id("aliasapplicanttitle"))
    aliasapplicanttitle.select_by_value(str(datalistfirst.aliastitleid))

    aliaslastname = driver.find_element_by_id("aliaslastname")
    aliaslastname.send_keys(datalistfirst.aliaslastname)

    aliasfirstname = driver.find_element_by_id("aliasfirstname")
    aliasfirstname.send_keys(datalistfirst.aliasfirstname)

    aliasmiddlename = driver.find_element_by_id("aliasmiddlename")
    aliasmiddlename.send_keys(datalistfirst.aliasmiddlename)
else:
    radioElement = driver.find_element_by_id("othernameflagno")
    radioElement.click()



gender = Select(driver.find_element_by_id("gender"))
gender.select_by_value(str(datalistfirst.genderid))


dateofbirth = driver.find_element_by_xpath("//*[@id='dateofbirth']")
dateofbirthrev = '-'.join(datalistfirst.dateofbirth.split('-')[::-1])
dateofbirth.send_keys(dateofbirthrev)
#dateofbirthlist =datalistfirst.dateofbirth.split('-')
#dateofbirthstring=''
#dateofbirthcombo = dateofbirthstring.join(dateofbirthlist)
#ActionChains(driver).move_to_element(dateofbirth).click().send_keys(dateofbirthcombo).perform()
print(dateofbirthrev)

fatherlastname = driver.find_element_by_id("fatherlastname")
fatherlastname.send_keys(datalistfirst.fatherlastname)

fatherfirstname = driver.find_element_by_id("fatherfirstname")
fatherfirstname.send_keys(datalistfirst.fatherfirstname)

fathermiddlename = driver.find_element_by_id("fathermiddlename")
fathermiddlename.send_keys(datalistfirst.fathermiddlename)

motherlastname = driver.find_element_by_id("motherlastname")
motherlastname.send_keys(datalistfirst.motherlastname)

motherfirstname = driver.find_element_by_id("motherfirstname")
motherfirstname.send_keys(datalistfirst.motherfirstname)

mothermiddlename = driver.find_element_by_id("mothermiddlename")
mothermiddlename.send_keys(datalistfirst.mothermiddlename)

if datalistfirst.selectparent!=1:
    radioElement = driver.find_element_by_id("selectparentmother")
    radioElement.click()
else:
    radioElement = driver.find_element_by_id("selectparentfather")
    radioElement.click()
#selectparentfather = driver.find_element_by_id("selectparentfather")
#selectparentmother = driver.find_element_by_id("selectparentmother")

residenceflataddress = driver.find_element_by_id("residenceflataddress")
residenceflataddress.send_keys(datalistfirst.residenceflataddress)

residencebuildingaddress = driver.find_element_by_id("residencebuildingaddress")
residencebuildingaddress.send_keys(datalistfirst.residencebuildingaddress)

residencestreetaddress = driver.find_element_by_id("residencestreetaddress")
residencestreetaddress.send_keys(datalistfirst.residencestreetaddress)

residencearea = driver.find_element_by_id("residencearea")
residencearea.send_keys(datalistfirst.residencearea)

residencetown = driver.find_element_by_id("residencetown")
residencetown.send_keys(datalistfirst.residencetown)


residencestate = driver.find_element_by_id("residencestate")
residencestate.send_keys(datalistfirst.residencestate)

residencepincode = driver.find_element_by_id("residencepincode")
residencepincode.send_keys(datalistfirst.residencepincode)

officename = driver.find_element_by_id("officename")
officename.send_keys(datalistfirst.officename)

officeflataddress = driver.find_element_by_id("officeflataddress")
officeflataddress.send_keys(datalistfirst.officeflataddress)

officebuildingaddress = driver.find_element_by_id("officebuildingaddress")
officebuildingaddress.send_keys(datalistfirst.officebuildingaddress)

officestreetaddress = driver.find_element_by_id("officestreetaddress")
officestreetaddress.send_keys(datalistfirst.officestreetaddress)

officearea = driver.find_element_by_id("officearea")
officearea.send_keys(datalistfirst.officearea)

officetown = driver.find_element_by_id("officetown")
officetown.send_keys(datalistfirst.officetown)

officestate = driver.find_element_by_id("officestate")
officestate.send_keys(datalistfirst.officestate)

officepincode = driver.find_element_by_id("officepincode")
officepincode.send_keys(datalistfirst.officepincode)

#addressofcommres = driver.find_element_by_id("addressofcommres")
if datalistfirst.addressofcommunication!=1:
    radioElement = driver.find_element_by_id("addressofcommoffice")
    radioElement.click()
else:
    radioElement = driver.find_element_by_id("addressofcommres")
    radioElement.click()
    
#addressofcommoffice = driver.find_element_by_id("addressofcommoffice")

countrycode = driver.find_element_by_id("countrycode")
countrycode.send_keys(datalistfirst.countrycode)

stdcode = driver.find_element_by_id("stdcode")
stdcode.send_keys(datalistfirst.stdcode)

mobilenumber = driver.find_element_by_id("mobilenumber")
mobilenumber.send_keys(datalistfirst.mobilenumber)

emailid = driver.find_element_by_id("emailid")
#Element not intercatable ERRORR
emailid.send_keys(datalistfirst.emailid)

'''representativetitle = driver.find_element_by_id("representativetitle")
representativelastname = driver.find_element_by_id("representativelastname")
representativefirstname = driver.find_element_by_id("representativefirstname")
representativemiddlename = driver.find_element_by_id("representativemiddlename")
representativeflataddress = driver.find_element_by_id("representativeflataddress")
representativebuildingaddress = driver.find_element_by_id("representativebuildingaddress")
representativestreetaddress = driver.find_element_by_id("representativestreetaddress")
representativearea = driver.find_element_by_id("representativearea")
representativetown = driver.find_element_by_id("representativetown")
representativestate = driver.find_element_by_id("representativestate")
representativepincode = driver.find_element_by_id("representativepincode")'''

statusofapplicantid = Select(driver.find_element_by_id("statusofapplicant"))
statusofapplicantid.select_by_value(str(datalistfirst.statusofapplicantid))

sourceofincomeid = Select(driver.find_element_by_id("sourceofincome"))
sourceofincomeid.select_by_value(str(datalistfirst.sourceofincomeid))

registrationnumber = driver.find_element_by_id("registrationnumber")
registrationnumber.send_keys(datalistfirst.registrationnumber)

adharnumber = driver.find_element_by_id("adharnumber")
adharnumber.send_keys(datalistfirst.adharnumber)

adharname = driver.find_element_by_id("adharname")
adharname.send_keys(datalistfirst.adharenrollmentid)

proofofidentityid = Select(driver.find_element_by_id("proofofidentity"))
proofofidentityid.select_by_value(str(datalistfirst.proofofidentityid))

proofofdateofbirthid = Select(driver.find_element_by_id("proofofbirth"))
proofofdateofbirthid.select_by_value(str(datalistfirst.proofofdateofbirthid))

proofofaddressid = Select(driver.find_element_by_id("proofofaddress"))
proofofaddressid.select_by_value(str(datalistfirst.proofofaddressid))

applicantplace = driver.find_element_by_id("applicantplace")
applicantplace.send_keys(datalistfirst.applicantplace)

todaydate = driver.find_element_by_xpath("//*[@id='todaydate']")
todaydaterev = '-'.join(datalistfirst.todaydate.split('-')[::-1])
todaydate.send_keys(todaydaterev)

pansubmit = driver.find_element_by_id("pansubmit")
#search_field.send_keys("Hello World")
#search_field.submit()
#driver.close()

