########################################################
#
#  SNowSerpent Main
#
#  Main routine of SNowSerpent
#
########################################################

import SNowParser as sp
import RESTActions as REST
import numpy as np

import argparse

def main():
    
    print("Welcome to SNowSerpent v0.1")
    print("\nExtracting data from ServiceNow")
    # urls of SNow Dev. instance for user and incident tables
    url_inc = 'https://dev61319.service-now.com/api/now/table/inicident'
    url_user = 'https://dev61319.service-now.com/api/now/table/sys_user'

    # extracted json strings of all users and incidents
    json_incidents = REST.get(url_inc)
    json_users = REST.get(url_user)

    print("-------")
    print("done")
    print("-------\n")

    print("Parsing data to CSV format")

    # parser for JSON -> CSV conversion
    Parser = sp.SNowParser()

    #ErrorCode Array for parsing routine
    ErrorCode = np.zeros(2)

    # parsing incidents and users
    pInc,ErrCode[0] = Parser.parse(json_incidents,type = "incident")
    pUser,ErrCode[1] = Parser.parse(json_users,type = "user")

    parsingSuccessful = pInc and pUser

    if not(parsingSuccessful):
        print("Parsing failed")    



    # send data back to ServiceNow
    REST.post(url,data)
    
    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    main()