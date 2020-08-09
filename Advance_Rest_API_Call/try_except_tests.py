import requests


try:
    response = requests.get('https://www.google.com/', timeout=0.5)
    response.raise_for_status()
    # Code here will only run if the request is successful
    print(response.headers)
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)