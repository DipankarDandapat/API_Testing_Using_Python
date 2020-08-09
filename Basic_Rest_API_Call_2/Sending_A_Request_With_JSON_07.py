import requests

#r = requests.get('https://requestb.in/wpo4xjwp')



#r = requests.get('https://requestb.in/wpo4xjwp?key1=value1&key2=value2')


#r = requests.post('https://requestb.in/wpo4xjwp')



payload = {'name' : 'Anthony', 'job' : 'Programmer'}
r = requests.post('https://reqres.in/api/users', json=payload)
print(r)
print(r.text)