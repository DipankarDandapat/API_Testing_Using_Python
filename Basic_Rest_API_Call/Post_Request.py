import requests
import json
import jsonpath

URL='https://reqres.in/api/users'

#read ther json file
file=open("E:\\PycharmProjects\\PyTestProject\\Api_Testing\\PostRequest.json", 'r')
json_data=file.read()#returns string data
#Convert string data to json format
input_json=json.loads(json_data)

#Make the post request with
response=requests.post(URL,input_json)
print("response",response.status_code)

#or

response_1=requests.post(URL, data = {"name": "morpheus", "job": "leader"})
print("response_1",response_1.status_code)

#or

payload = {"name": "morpheus", "job": "leader"}
response_2=requests.post(URL,data=json.dumps(payload))
print("response_2", response_2.status_code)

#or

payload = {"name": "morpheus", "job": "leader"}
response_3=requests.post(URL,json=payload)
print("response_3", response_3.status_code)



print(response.content)
print(response.headers)
print(response.headers.get('Content-Length'))
print(response.encoding)
print(response.elapsed)
print(response.cookies)

#Convert response text format to json format
json_Formet=json.loads(response.text)
print(json_Formet)

#Validate Response
user_id=jsonpath.jsonpath(json_Formet,'id')
print(user_id[0])

print(response.text)