import json

data = {
    "user":{
        "name" : "Vincent Deneyer",
        "age" : 54
        }
}
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent = 4)
