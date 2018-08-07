import sys          # to handle argument values
import requests     # to make get/post requests
# ignore insecure https requests warning:
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# head is a JSON object that holds API key information
head = {    'apiKey' : 'MDKu7n6PQENni3goRuQjvTQJGD3UBCYp',
            'Content-Type' : 'application/json' }
mod = sys.argv[1] # 1st argument = module number
chn = sys.argv[2] # 2nd argument = channel number
# construct request URL for the 'local' built-in rack of I/O *status*
url = 'https://opto-03-f6-41/manage/api/v1/io/local/modules/'+mod+'/channels/'+chn+'/digital/status'
print('Reading value at output ' + chn + ' on module ' + mod)
# make the RESTful get request and save the response
response = requests.get(url, headers=head, verify=False)
# output the result:
print (response)
print (response.content)
print (response.text)
print (response.json)