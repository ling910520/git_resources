import requests
import json
url = 'http://localhost:3003/writeToUsers'
header = {'Content-Type': 'application/json'}
data = {"a":1}
response = requests.post(url,data=data,headers=header)
print(response.text)

data='01010101011'
data = [int(s) for s in data][::-1]
data