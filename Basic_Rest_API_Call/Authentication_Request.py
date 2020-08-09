import requests
from requests.auth import HTTPBasicAuth

response=requests.get('https://api.github.com/user', auth=HTTPBasicAuth('d.dandapat96@gmail.com', 'Dipankar1994@'))
print(response.status_code)
#or
response1=requests.get('https://api.github.com/user', auth=('d.dandapat96@gmail.com', 'Dipankar1994@'))
print(response1.status_code)

print(response.content)#Fetch content
print(response.headers)#Fetch headers
print(response.headers.get('Content-Type'))#Fetch headers Content-Type
print(response.headers['Content-Type'])#Fetch headers Content-Type
print(response.cookies)#Fetch cookies
print(response.encoding)#Fetch encoding
print(response.history)#Fetch history
print(response.elapsed)#Fetch elapsed