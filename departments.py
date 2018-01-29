# Outputs an HTML table listing the total number of equipment bookings in your system by department for the current date

import  requests, json
from json2html import *
import itertools 
from operator import itemgetter

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

# Enter the Question ID for the question on your form pertaining to department 
input = sorted(input, key=itemgetter('[ENTER QUESTION ID HERE]'))

departments = []
for key, value in itertools.groupby(input, key=itemgetter('[ENTER QUESTION ID HERE]')):
    dept = {}
    dept['Department Name'] = key
    total_reservations = 0
    for i in value:
        total_reservations += 1 
        dept['Total Equipment Bookings'] = total_reservations
    departments.append(dept)

my_json = json2html.convert(json = departments)

my_file = open("departments.html", 'w')
my_file.write(my_json)
my_file.close()