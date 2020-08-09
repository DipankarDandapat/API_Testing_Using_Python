import requests

#r = requests.get('https://requestb.in/wpo4xjwp')



#r = requests.post('https://requestb.in/wpo4xjwp')


payload = {'name' : 'Anthony', 'location' : 'Las Vegas'}
#r = requests.post('https://requestb.in/wpo4xjwp', data=payload)
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)