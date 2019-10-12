import mysql.connector
import re

class DatabaseHandle:
    mydb = None
    myCursor = None

    def __init__(self):
        #Initialise the Database with host, username, password
        self.mydb = mysql.connector.connect(host="localhost",
        user = "root",
        passwd = ""
        )
        self.myCursor = self.mydb.cursor()

    def databaseList(self):
        #List of Databases
        self.myCursor.execute("SHOW DATABASES")
        databaselist = list()
        for database in self.myCursor:
            databaselist.append(database[0])
        return databaselist

    def connectDatabase(self,databaseName):
        #Connect to the database First
        databaselist = self.databaseList()
        if databaseName in databaselist:
            self.mydb = mysql.connector.connect(host="localhost",
            user="root",
            passwd="",
            database = databaseName
            )
            self.myCursor = self.mydb.cursor()
            print("Database "+databaseName+" Connected")
        else:
            print("Database "+databaseName+" does not exist's")

    def createDatabase(self,databaseName):
        #Create database
        try:
            self.myCursor.execute("CREATE DATABASE "+databaseName)
        except Exception as e:
            print(" "+str(e))

    def dropDatabase(self,databaseName):
        try:
            self.myCursor.execute("DROP DATABASE "+databaseName)
            print('Database Deleted '+databaseName)
        except Exception as e:
            print(" "+str(e))
    
    def currentDatabase(self):
        try:
            self.myCursor.execute("SELECT database()")
            database = [db[0] for db in self.myCursor]
            return database[0]
        except Exception as e:
            print(e)

class TableHandle(DatabaseHandle):
        def __init__(self,dObject):
            if dObject.currentDatabase() is None:
                self.table = None
            else:
                self.table = dObject.myCursor

        def isDatabaseConnected(self):
            if self.table is None:
                return False
            else:
                return True

        def tableList(self):
            #List of tables
            try:
                if self.isDatabaseConnected():
                    self.table.execute("SHOW TABLES")
                    tablelist = list()
                    for table in self.table:
                        tablelist.append(table)
                    return tablelist
                else:
                    print("No database Selected")

            except Exception as e:
                print(e)



dObject = DatabaseHandle()
print(dObject.databaseList())
tObject = TableHandle(dObject)
tObject.tableList()