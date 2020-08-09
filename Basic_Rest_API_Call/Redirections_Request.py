"""Redirection in HTTP means forwarding the network request to a different URL.
For example, if we make a request to "http://www.github.com",
it will redirect to "https://github.com" using a 301 redirect."""



import requests
import json
import jsonpath

r = requests.post("http://www.github.com")
print(r.url)
print(r.history)
print(r.status_code)