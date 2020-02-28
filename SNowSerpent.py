########################################################
#
#  SNowSerpent Main
#
#  Main routine of SNowSerpent
#
########################################################

import SNowParser as sp
import GetType as gt
import RESTActions as REST


import numpy as np


import argparse

def main(verbose = False):
    
    print("Welcome to SNowSerpent v0.1")
    print("\nExtracting data from ServiceNow")
    
    # extract table of choice from config file
    TypeDefinition = gt.TypeLoader()
    table = TypeDefinition.getTableType()
    fields = TypeDefinition.getFields()

    # urls of SNow Dev. instance for user and incident tables
    url_choice = 'https://dev61319.service-now.com/api/now/table/' + table
    url_user = 'https://dev61319.service-now.com/api/now/table/sys_user'

    # extracted json strings of all users and incidents
    json_choice = REST.get(url_choice)
    json_users = REST.get(url_user)

    with open("tmp.json","w+") as f:
        for j in json_choice['result']:
            f.write(str(j)+"\n")
    

    print("-------")
    print("done")
    print("-------\n")

    print("Parsing data to CSV format")

    # parser for JSON -> CSV conversion
    Parser = sp.SNowParser()

    #ErrorCode Array for parsing routine
    ErrCode = ["",""]

    # parsing incidents and users
    pInc,ErrCode[0] = Parser.parse(json_choice,table,fieldsOfInterest = fields,type = True)
    pUser,ErrCode[1] = Parser.parse(json_users,"sys_user")

    parsingSuccessful = pInc and pUser

    if not(parsingSuccessful):
        print("Parsing failed")    



    # send data back to ServiceNow
    #REST.post(url,data)
    
    


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

    args = parser.parse_args()
    main(verbose=args.verbose)