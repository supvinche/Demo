import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

json_str = json.dumps(Person("will", 29))

print(json_str)