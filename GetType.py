########################################################
#
#  SNowSerpent GetType
#
#  loads config file of table and field
#  that is extracted from ServiceNow
#
########################################################


class TypeLoader:
    def __init__(self,fileName = "ConfigFiles/extract.config",verbose = False):
        self.__verbose = verbose
        self.__tableType = ""
        self.__fields = []
        self.__fileName = fileName

        self.__LoadData()

    def __LoadData(self):

        if self.__verbose:
            print("---------------------------")
            print("\nReading config file")

        # loading file
        try:
            with open(self.__fileName,'r') as file:
                lines = file.readlines()
                first = True
                for line in lines:
                    if self.__verbose:
                        print(line)
                    # remove \r,\n,etc. from line
                    line = line.rstrip()

                    # skip comments
                    if line[0] == '#':
                        continue
                    else:
                        # table name comes first in file
                        if first:
                            self.__tableType = line
                            first = False
                        
                        # read fields of interest
                        else:
                            self.__fields = line.split(",")
        except (OSError,IOError):
            print("File",self.__fileName,"not found")
        
        if self.__verbose:
            print("config file loaded")
            print("---------------------------")

    def getTableType(self):
        return self.__tableType
    
    def getFields(self):
        return self.__fields
