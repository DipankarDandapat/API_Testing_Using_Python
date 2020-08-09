import requests
import json
import jsonpath

URL='https://reqres.in/api/users?page=2'
#Send the request
response=requests.get(URL)


print(response.status_code)#Fetch status code
print(response.content)#Fetch content
print(response.headers)#Fetch headers
print(response.headers.get('Content-Type'))#Fetch headers Content-Type
print(response.headers['Content-Type'])#Fetch headers Content-Type
print(response.cookies)#Fetch cookies
print(response.encoding)#Fetch encoding
print(response.history)#Fetch history
print(response.elapsed)#Fetch elapsed
assert response.status_code==200 #Assert response status code
#Convert response text format to json format
json_Formet=json.loads(response.text)
print(json_Formet)
#Validate josn response data
#json path returns List of object
page=jsonpath.jsonpath(json_Formet,'total_pages')
assert  page[0] == 2
first_name=jsonpath.jsonpath(json_Formet,'data[0].first_name')
print(first_name[0])
# Get all the last_name value from the response
for i in range(0,3):
    last_name = jsonpath.jsonpath(json_Formet, 'data[' +str(i)+ '].last_name')
    print(last_name[0])


print(response.raw)
print(response.raw.read(10))
print(response.json())

print(response.status_code == requests.codes.ok)

print(response.raise_for_status())


print(response.url)

print(response.elapsed.total_seconds())

print(len(response.content))


