# Outputs a json file, an HTML file, and a csv file listing equipment bookings in your system for the current date

import  requests, json
from json2html import *

token_url  =  'https://api2.libcal.com/1.1/oauth/token'

test_api_url  =  'https://api2.libcal.com/1.1/equipment/bookings?formAnswers=1'

# Enter your credentials
client_id  =  '[ENTER CLIENT ID HERE]'
client_secret  = '[ENTER CLIENT SECRET HERE]'
 
data  =  { 'grant_type' :  'client_credentials' }
 
access_token_response  =  requests.post(token_url, data = data, verify = False , allow_redirects = False , auth = (client_id, client_secret))
 
tokens  =  json.loads(access_token_response.text) 
 
api_call_headers  =  { 'Authorization' :  'Bearer '  +  tokens[ 'access_token' ]}
api_call_response  =  requests.get(test_api_url, headers = api_call_headers, verify = False )

my_json = api_call_response.json()
print(my_json)

# Write json to json file
with open("libcal.json","w") as f:
    json.dump(my_json, f)

# Write json to an html file
my_html = json2html.convert(json = my_json)
print(my_html)

my_file = open("libcal.html", 'w')
my_file.write(my_html)
my_file.close()

# Create dataframe
df = pd.DataFrame(my_json)
print(df)

# Write dataframe to csv file
df.to_csv("libcal.csv")