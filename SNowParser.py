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
    def __init__(self,FileName,dataVault = "ParsedData",verbose = False):
        # directory for csv files
        self.__DataVault = dataVault
        self.__verbose = verbose
        # 
        self.__results = []
        self.__isIncident = True

        # load error code dictionary
        self.__ErrorCodes = errC.SNowErrorCodes()

    def parse(self,JSON,type = "incident"):

        # reset errors (to be safe)
        self.__ErrorCodes.reset()

        # check type of JSON
        self.__isIncident = type == "incident"
        
        # array of all extracted records of target table
        self.__results = JSON['result']

        # check if records were sent
        if len(self.__results) == 0:
            tmpErr = "101" if self.__isIncident else "102"
            self.__ErrorCodes.setError(tmpErr)
        else:    
            __parse()
    
        if self.__verbose:
            print("Error Code",errCode,"->",errMeaning)

        return 

    def __parse(self):
        

        if self.__isIncident:
            
        else: 
            names = [[record['name'],record['sys_id']] for record in self.__results]
        
        return noError,errCode


    def __writeToCsv(self):
        with 

    def __getCSVDirectory(self):
        return self.__DataVault
