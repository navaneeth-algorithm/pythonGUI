Classes present 
    DatabaseHandle
    TableHandle

DatabaseHandle
    Member Functions
        databaseList()
            Returns the list of database

        connectDatabase(databaseName)
            Connect to the database.If no Database is present then you have create database.

        createDatabase(databaseName)
            Create new database with databaseName.If same Name Already exists, error is popped up. 

        dropDatabase(databaseName)
            Drop the existsing database with databaseName

        currentDatabase()
            Return the existing database Name

TableHandle 
    It extends the DatabaseHandle.It takes database Object as parameter.
    Member Function
     tableList()
        This gives the list of table present in the database
