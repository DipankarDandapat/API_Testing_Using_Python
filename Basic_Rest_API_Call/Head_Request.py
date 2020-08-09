import requests
import json
import jsonpath

URL='https://reqres.in/api/users?page=2'
#Send the request
response=requests.head(URL)

print(response.status_code)
print(response.headers)




