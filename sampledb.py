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
        self.panname=''
        
        #Pan Database acesing
        self.database = DatabaseHandle()
        self.dblist = self.database.databaseList()
        self.database.connectDatabase('Pan')
        
        self.table = TableHandle(self.database)
        self.tables = self.table.tableList()
        #print(tables)

        self.query = self.table.QueryExecute("SELECT * From NewPan")
        
    def getPanData(self):
        
        self.pan_data_list = [PanData() for i in range(0,len(self.query))]
        for i in range(0,len(self.query)):
            queryList = list(self.query[i])
            self.pan_data_list[i] = PanData()
            self.pan_data_list[i].id=queryList[0]
            self.pan_data_list[i].titleid =queryList[1]
            self.pan_data_list[i].emailid =queryList[2]
            self.pan_data_list[i].genderid=queryList[3]
            self.pan_data_list[i].sourceofincomeid=queryList[4]
            self.pan_data_list[i].statusofapplicantid=queryList[5]
            self.pan_data_list[i].addressofcommunication=queryList[6]
            self.pan_data_list[i].assessingofficertype=queryList[7]
            self.pan_data_list[i].rangecode=queryList[8]
            self.pan_data_list[i].assessingtypeofficernumber=queryList[9]
            self.pan_data_list[i].firstname=queryList[10]
            self.pan_data_list[i].middlename=queryList[11]
            self.pan_data_list[i].lastname=queryList[12]
            self.pan_data_list[i].aliasfirstname=queryList[13]
            self.pan_data_list[i].aliasmiddlename=queryList[14]
            self.pan_data_list[i].aliaslastname=queryList[15]
            self.pan_data_list[i].aliastitleid=queryList[16]
            self.pan_data_list[i].dateofbirth=queryList[17]
            self.pan_data_list[i].fatherfirstname=queryList[18]
            self.pan_data_list[i].fathermiddlename=queryList[19]
            self.pan_data_list[i].fatherlastname=queryList[20]
            self.pan_data_list[i].motherfirstname=queryList[21]
            self.pan_data_list[i].mothermiddlename=queryList[22]
            self.pan_data_list[i].motherlastname=queryList[23]
            self.pan_data_list[i].residenceflataddress=queryList[24]
            self.pan_data_list[i].residencebuildingaddress=queryList[25]
            self.pan_data_list[i].residencestreetaddress=queryList[26]
            self.pan_data_list[i].residencearea=queryList[27]
            self.pan_data_list[i].residencetown=queryList[28]
            self.pan_data_list[i].residencestate=queryList[29]
            self.pan_data_list[i].residencepincode=queryList[30]
            self.pan_data_list[i].officename=queryList[31]
            self.pan_data_list[i].officeflataddress=queryList[32]
            self.pan_data_list[i].officebuildingaddress=queryList[33]
            self.pan_data_list[i].officestreetaddress=queryList[34]
            self.pan_data_list[i].officearea=queryList[35]
            self.pan_data_list[i].officetown=queryList[36]
            self.pan_data_list[i].officestate=queryList[37]
            self.pan_data_list[i].officepincode=queryList[38]
            self.pan_data_list[i].countrycode=queryList[39]
            self.pan_data_list[i].areacode=queryList[40]
            self.pan_data_list[i].mobilenumber=queryList[41]
            self.pan_data_list[i].registrationnumber=queryList[42]
            self.pan_data_list[i].adharnumber=queryList[43]
            self.pan_data_list[i].adharenrollmentid=queryList[44]
            self.pan_data_list[i].representativefirstname=queryList[45]
            self.pan_data_list[i].representativemiddlename=queryList[46]
            self.pan_data_list[i].representativelastname=queryList[47]
            self.pan_data_list[i].representativetitleid=queryList[48]
            self.pan_data_list[i].representativeflataddress=queryList[49]
            self.pan_data_list[i].representativebuildingaddress=queryList[50]
            self.pan_data_list[i].representativestreetaddress=queryList[51]
            self.pan_data_list[i].representativearea=queryList[52]
            self.pan_data_list[i].representativetown=queryList[53]
            self.pan_data_list[i].representativestate=queryList[54]
            self.pan_data_list[i].representativepincode=queryList[55]
            self.pan_data_list[i].proofofidentityid=queryList[56]
            self.pan_data_list[i].proofofaddressid=queryList[57]
            self.pan_data_list[i].proofofdateofbirthid=queryList[58]
            self.pan_data_list[i].applicantplace=queryList[59]
            self.pan_data_list[i].todaydate=queryList[60]
            self.pan_data_list[i].panname=queryList[61]
            self.pan_data_list[i].stdcode=queryList[62]
            self.pan_data_list[i].selectparent=queryList[63]
       #Return Entire PanData 
        return self.pan_data_list
    
    def getPanDatai(self,i):
        pandata = self.getPanData()
        return pandata[i]