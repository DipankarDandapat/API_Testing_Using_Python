import requests
from requests.auth import HTTPBasicAuth



r = requests.get('https://httpbin.org/basic-auth/anthony/secret', auth=HTTPBasicAuth('anthony', 'secret'))
print(r)