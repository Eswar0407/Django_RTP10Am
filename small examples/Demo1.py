import json

file = open("Demo.json","r")
json_string = file.read()
print(json_string)

# convert the string to dict
# to convert jsonstring to dict we use "loads" function from json

json_data = json.loads(json_string)
print(json_data)
