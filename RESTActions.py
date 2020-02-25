import requests
import json


def get(url,user = "admin",pwd = "admin"):
     # Set proper headers
    headers = {"Accept":"application/json"}
    
    # Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers )
    # Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    return response.json()

def post(url,data,user = "admin",pwd = "admin"):
    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    
    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=data)
    
    # Check for HTTP codes other than 200
    if response.status_code != 201: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()