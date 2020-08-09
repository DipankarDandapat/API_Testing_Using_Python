import requests


'''
r = requests.get('https://httpbin.org/status/501')

try:
    r.raise_for_status()
except requests.exceptions.HTTPError:
    print('ERROR! ERROR! ERROR!')

print(r)
'''


try:
    r = requests.get('https://dsklfjdslfudsfdsj.com')
except requests.exceptions.ConnectionError:
    print('CONNECTION ERROR!')