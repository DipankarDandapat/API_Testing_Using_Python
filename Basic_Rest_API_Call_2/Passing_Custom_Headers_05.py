import requests

#r = requests.get('https://requestb.in/wpo4xjwp')

#r = requests.get('https://requestb.in/wpo4xjwp?key1=value1&key2=value2')


headers = {'my-token' : '329uljsdf9f84oijrljfwe908u23orijdsk09asuioijr4ufeswijf39', 'User-Agent' : 'fake agent'}
r = requests.get('https://requestb.in/wpo4xjwp', headers=headers)