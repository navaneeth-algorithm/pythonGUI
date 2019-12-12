# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:48:10 2019

@author: hp
"""
class PanData:
from pythonDatabase import DatabaseHandle,TableHandle

database = DatabaseHandle()
dblist = database.databaseList()
database.connectDatabase('Pan')

table = TableHandle(database)
tables = table.tableList()
#print(tables)
query = table.QueryExecute("SELECT * From NewPan")
for i in range(0,len(query)):
    queryList = list(query[i])
    print(queryList)

