import json
data = {"student":{"name":"Somavarapu Eswar","marks":456,"status":False}}

file = open("student1.json","w")

json.dump(data,file)

file.close()
print("File Created and Data Written")
