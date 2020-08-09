import requests

response = requests.get('http://www.google.com', timeout=0.7)

print(response.status_code)

r = requests.get('https://smartops.vlabsinc.com/login', verify=True)

print(r.status_code)