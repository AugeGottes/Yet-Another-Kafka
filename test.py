import json
 
# # Data to be written
# dictionary = {
#     "hello":"lol"
# }
 
# # Serializing json
# json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
# with open("sample.json", "a") as outfile:
#     outfile.write(json_object)
filename="sample.json"
entry={'hello','lol1'}
with open(filename, "r") as file:
    data = json.load(file)
# 2. Update json object
data.append(entry)
# 3. Write json file
with open(filename, "w") as file:
    json.dump(data, file)