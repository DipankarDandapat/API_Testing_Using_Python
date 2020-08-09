import requests

#r = requests.get('https://requestb.in/wpo4xjwp')


#r = requests.post('https://requestb.in/wpo4xjwp')



'''
files = {'file' : open('cat.jpg', 'rb')}
r = requests.post('https://requestb.in/wpo4xjwp', files=files)
'''

files = {'file' : ('cat.jpg', open('cat.jpg', 'rb'), 'image/jpeg')}
r = requests.post('https://requestb.in/wpo4xjwp', files=files)