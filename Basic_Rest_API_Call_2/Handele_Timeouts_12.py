import requests


try:
    r = requests.get('https://httpbin.org/delay/10', timeout=5)
except requests.exceptions.ReadTimeout:
    print('TIMED OUT!!!')