import requests as reqs

cookie = {'username':'Pavneet'}
response = reqs.get('https://postman-echo.com/cookies/set',cookies = cookie)   # send cookie
print(response.text)  # output: {"cookies":{"username":"Pavneet"}}

print(response.status_code)
