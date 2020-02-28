########################################################
#
#  SNowSerpent Parser
#
#  Transform REST API JSON to CSV format of
#  data analysis objects
#
########################################################


import numpy as np
import ErrorCodes as errC

class SNowParser:
    def __init__(self,verbose = False):
        # directory for csv files
        self.__verbose = verbose
        # 
        self.__names = []
        self.__results = []
        self.__isChoice = True

        # load error code dictionary
        self.__ErrorCodes = errC.SNowErrorCodes()
        self.__fields = []
        
        self.__AmountOfRecords = 0
        self.__AmountOfFields = 0
        self.__allPresent = True

    def parse(self,JSON,parserName,fieldsOfInterest = "",type = False,tableName = "user"):
        
        self.__parserName = parserName

        # if input JSON is not user table
        if type:
            self.__tableName = tableName

        # set fields of interest for extraction
        self.__fields = fieldsOfInterest

        # reset active errors (to be safe)
        self.__ErrorCodes.reset()

        # check type of JSON
        self.__isChoice = type
        
        # array of all extracted records of target table
        self.__results = JSON['result']
        #print(self.__results)

        # validate that all field labels of interest are
        # present in json 
        self.__checkCorrectFields()
        if not(self.__allPresent):
            self.__ErrorCodes.setError("103")



        # get respective lengths of record and field arrays
        self.__AmountOfRecords = len(self.__results)
        self.__AmountOfFields = len(self.__fields)

        # check if records were sent
        if self.__AmountOfRecords == 0:
            tmpErr = "101" if self.__isChoice else "102"
            self.__ErrorCodes.setError(tmpErr)
        elif self.__allPresent:    
            self.__parseTable()
        
        errCode,errMeaning = self.__ErrorCodes.getError()
        passed = errCode == "100"
        if not(passed):
            print(self.__parserName + ": Error Code",errCode,"->",errMeaning)

        return passed,errCode

    def __parseTable(self):
        # extract records with respective fields of interest
        if self.__isChoice:            
            self.__Records = np.zeros((self.__AmountOfRecords,self.__AmountOfFields),dtype = str)
            # loop over all records in json file
            for i,record in enumerate(self.__results):
                # loop over all fields of interest in fields array
                for j,field in enumerate(self.__fields):
                    self.__Records[i,j] = record[field]
        else: 
            self.__names = [[record['name'],record['sys_id']] for record in self.__results]
        
        self.__writeToCsv()

    def __checkCorrectFields(self):
        # validate that all fields labels of interest
        # are present in extracted json
        for field in self.__fields:
            fieldFound = False
            # compare defined field value to all field labels in json
            for fieldValue in self.__results[0]:
                fieldFound = field == fieldFound
                if fieldFound:
                    break
            if not(fieldFound):
                self.__allPresent = False
                print("ERROR: Field",field,"not found in json file!")
                return

    def __writeToCsv(self):
        directory = "ParsedData/"
        fileTmp = "ExtractedRecords.csv" if self.__isChoice else "ExtractedUsers.csv"
        fileName = directory + fileTmp
        try:
            with open(fileName,"w+") as file:
                file.write("# Extracted file from ServiceNow")
                file.write("# table: " + self.__getTableName())
                file.write("# fields: " + self.__getFieldsString())
                file.write("#")
                self.__writeContents(file)

        except(OSError,IOError):
            print("Could not open",fileName)

    def __getTableName(self) -> str:
        return self.__tableName if self.__isChoice else "sys_user"

    def __getFieldsString(self) -> str:
        if not(self.__isChoice):
            return "name,sys_id"
        else:
            tmpString = ""
            for i,s in enumerate(self.__fields):
                tmpString += s 
                if i < len(self.__fields) - 1:
                    tmpString += ", "
            return tmpString

    def __writeContents(self,file):
        writeRecord = self.__Records if self.__isChoice else self.__names
        for record in writeRecord:
            line = ""
            for i,field in enumerate(record):
                line += field
                if i < len(record) - 1:
                    line += ","
            file.write(line)