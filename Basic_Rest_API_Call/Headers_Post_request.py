import requests

headers = {
'Authorization': 'Bearer API_KEY',
'Content-Type': 'application/json',
}

data = '{"records": [{"fields": {"Drink": "Black Decaf Tea"}}]}'

res = requests.post('https://cat-fact.herokuapp.com/facts', headers=headers, data=data)

print(res.json())