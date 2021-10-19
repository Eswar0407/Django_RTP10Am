import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/")

#print(response.status_code)

#print(response.text)
list_data = json.loads(response.text)
print(list_data)
print(len(list_data))
print(list_data[0])
print(list_data[-1])