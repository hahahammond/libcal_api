# Outputs an HTML table listing equipment bookings in your system for the current date

import  requests, json
from json2html import *

token_url  =  'https://api2.libcal.com/1.1/oauth/token'

test_api_url  =  'https://api2.libcal.com/1.1/equipment/bookings?formAnswers=1'

# Enter your credentials
client_id  =  '[ENTER CLIENT ID HERE]'
client_secret  =  '[ENTER CLIENT SECRET HERE]'
 
data  =  { 'grant_type' :  'client_credentials' }
 
access_token_response  =  requests.post(token_url, data = data, verify = False , allow_redirects = False , auth = (client_id, client_secret))
 
tokens  =  json.loads(access_token_response.text) 
 
api_call_headers  =  { 'Authorization' :  'Bearer '  +  tokens[ 'access_token' ]}
api_call_response  =  requests.get(test_api_url, headers = api_call_headers, verify = False )
print(api_call_response.json())

input = api_call_response.json()
my_json = json2html.convert(json = input)
print(my_json)

my_file = open("libcal.html", 'w')
my_file.write(my_json)
my_file.close()
