########################################################
#
#  SNowSerpent ErrorCodes
#
#  parser error code collection and handler
# 
########################################################


class SNowErrorCodes:

    def __init__(self):
        # set dictionary of errors
        self.__ErrorDict = self.__setDictionary()
        
        # default: no error
        self.__activeError = '100'        

    def __setDictionary(self) -> dict:
        D = {
            '100': 'no error',
            '101': 'no incidents found',
            '102': 'no users found',
            '103': 'unknown error'
        }
        return D


    def setError(self,error: str):
        self.__activeError = error

    def getError(self):
        dictEntry = self.__ErrorDict[self.__activeError]
        return self.__activeError,dictEntry

    def reset(self):
        self.__activeError = '100'