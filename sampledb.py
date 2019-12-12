# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:48:10 2019

@author: hp
"""

from pythonDatabase import DatabaseHandle,TableHandle


class PanData:
    def __init__(self):
        self.id=''
        self.titleid =''
        self.emailid =''
        self.genderid=''
        self.sourceofincomeid=''
        self.statusofapplicantid=''
        self.addressofcommunication=''
        self.assessingofficertype=''
        self.rangecode=''
        self.assessingtypeofficernumber=''
        self.firstname=''
        self.middlename=''
        self.lastname=''
        self.aliasfirstname=''
        self.aliasmiddlename=''
        self.aliaslastname=''
        self.aliastitleid=''
        self.dateofbirth=''
        self.fatherfirstname=''
        self.fathermiddlename=''
        self.fatherlastname=''
        self.motherfirstname=''
        self.mothermiddlename=''
        self.motherlastname=''
        self.residenceflataddress=''
        self.residencebuildingaddress=''
        self.residencestreetaddress=''
        self.residencearea=''
        self.residencetown=''
        self.residencestate=''
        self.residencepincode=''
        self.officename=''
        self.officeflataddress=''
        self.officebuildingaddress=''
        self.officestreetaddress=''
        self.officearea=''
        self.officetown=''
        self.officestate=''
        self.officepincode=''
        self.countrycode=''
        self.areacode=''
        self.mobilenumber=''
        self.registrationnumber=''
        self.adharnumber=''
        self.adharenrollmentid=''
        self.representativefirstname=''
        self.representativemiddlename=''
        self.representativelastname=''
        self.representativetitleid=''
        self.representativeflataddress=''
        self.representativebuildingaddress=''
        self.representativestreetaddress=''
        self.representativearea=''
        self.representativetown=''
        self.representativestate=''
        self.representativepincode=''
        self.proofofidentityid=''
        self.proofofaddressid=''
        self.proofofdateofbirthid=''


database = DatabaseHandle()
dblist = database.databaseList()
database.connectDatabase('Pan')

table = TableHandle(database)
tables = table.tableList()
#print(tables)

query = table.QueryExecute("SELECT * From NewPan")
pan_data_list = [PanData() for i in range(0,len(query))]
for i in range(0,len(query)):
    queryList = list(query[i])
    pan_data_list[i] = PanData()
    pan_data_list[i].id=queryList[0]
    pan_data_list[i].titleid =queryList[1]
    pan_data_list[i].emailid =queryList[2]
    pan_data_list[i].genderid=queryList[3]
    pan_data_list[i].sourceofincomeid=queryList[4]
    pan_data_list[i].statusofapplicantid=queryList[5]
    pan_data_list[i].addressofcommunication=queryList[6]
    pan_data_list[i].assessingofficertype=queryList[7]
    pan_data_list[i].rangecode=queryList[8]
    pan_data_list[i].assessingtypeofficernumber=queryList[9]
    pan_data_list[i].firstname=queryList[10]
    pan_data_list[i].middlename=queryList[11]
    pan_data_list[i].lastname=queryList[12]
    pan_data_list[i].aliasfirstname=queryList[13]
    pan_data_list[i].aliasmiddlename=queryList[14]
    pan_data_list[i].aliaslastname=queryList[15]
    pan_data_list[i].aliastitleid=queryList[16]
    pan_data_list[i].dateofbirth=queryList[17]
    pan_data_list[i].fatherfirstname=queryList[18]
    pan_data_list[i].fathermiddlename=queryList[19]
    pan_data_list[i].fatherlastname=queryList[20]
    pan_data_list[i].motherfirstname=queryList[21]
    pan_data_list[i].mothermiddlename=queryList[22]
    pan_data_list[i].motherlastname=queryList[23]
    pan_data_list[i].residenceflataddress=queryList[24]
    pan_data_list[i].residencebuildingaddress=queryList[25]
    pan_data_list[i].residencestreetaddress=queryList[26]
    pan_data_list[i].residencearea=queryList[27]
    pan_data_list[i].residencetown=queryList[28]
    pan_data_list[i].residencestate=queryList[29]
    pan_data_list[i].residencepincode=queryList[30]
    pan_data_list[i].officename=queryList[31]
    pan_data_list[i].officeflataddress=queryList[32]
    pan_data_list[i].officebuildingaddress=queryList[33]
    pan_data_list[i].officestreetaddress=queryList[34]
    pan_data_list[i].officearea=queryList[35]
    pan_data_list[i].officetown=queryList[36]
    pan_data_list[i].officestate=queryList[37]
    pan_data_list[i].officepincode=queryList[38]
    pan_data_list[i].countrycode=queryList[39]
    pan_data_list[i].areacode=queryList[40]
    pan_data_list[i].mobilenumber=queryList[41]
    pan_data_list[i].registrationnumber=queryList[42]
    pan_data_list[i].adharnumber=queryList[43]
    pan_data_list[i].adharenrollmentid=queryList[44]
    pan_data_list[i].representativefirstname=queryList[45]
    pan_data_list[i].representativemiddlename=queryList[46]
    pan_data_list[i].representativelastname=queryList[47]
    pan_data_list[i].representativetitleid=queryList[48]
    pan_data_list[i].representativeflataddress=queryList[49]
    pan_data_list[i].representativebuildingaddress=queryList[50]
    pan_data_list[i].representativestreetaddress=queryList[51]
    pan_data_list[i].representativearea=queryList[52]
    pan_data_list[i].representativetown=queryList[53]
    pan_data_list[i].representativestate=queryList[54]
    pan_data_list[i].representativepincode=queryList[55]
    pan_data_list[i].proofofidentityid=queryList[56]
    pan_data_list[i].proofofaddressid=queryList[57]
    pan_data_list[i].proofofdateofbirthid=queryList[58]
        
    #print(queryList)

print(pan_data_list[0].firstname)