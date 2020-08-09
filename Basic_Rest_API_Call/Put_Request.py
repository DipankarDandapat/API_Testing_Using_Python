#pip install responses
#pip install jsonpath
import requests
import json
import jsonpath

URL='https://reqres.in/api/users/2'

#read ther json file
file=open("E:\\PycharmProjects\\PyTestProject\\Api_Testing\\PostRequest.json", 'r')
json_data=file.read()#returns string data
input_json=json.loads(json_data)# converted string data to json data

#Make the Put request with input_json
response=requests.put(URL,input_json)

print(response.status_code)
print(response.content)
#Convert response text format to json format
josn_formet=json.loads(response.text)
print(josn_formet)
#Validate Json path value
user_name=jsonpath.jsonpath(josn_formet,'name')
print(user_name[0])
