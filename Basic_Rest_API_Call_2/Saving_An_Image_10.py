import requests

#r = requests.get('https://requestb.in/wpo4xjwp')

#r = requests.post('https://requestb.in/wpo4xjwp')


r = requests.get('https://httpbin.org/image/jpeg')
print(r.headers)

with open('image.jpg', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=500):
        fd.write(chunk)