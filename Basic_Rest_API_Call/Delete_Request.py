#pip install responses
import requests


URL='https://reqres.in/api/users/2'
#Send the delete request
response=requests.delete(URL)

print(response.status_code)#Fetch status code
print(response.content)#Fetch content
print(response.headers)#Fetch headers
print(response.headers.get('Content-Type'))#Fetch headers Content-Type
print(response.cookies)#Fetch cookies
print(response.encoding)#Fetch encoding
print(response.history)#Fetch history
print(response.elapsed)#Fetch elapsed

URL='https://reqres.in/api/users?page=2'
#Send the request
response=requests.get(URL)