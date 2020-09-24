import json


# ----------using json with strings----------
json_string = """
{
  "people": [
    {
      "name": "can",

      "phone": "0555-555-55-55",

      "email": "null"
    },
    {
      "name": "not can",

      "phone": "0444-444-44-44",

      "email": "hi@himail.com"
    }
    ]
}
"""
# load json from string
data  = json.loads(json_string)

# modify json
for person in data["people"]:
    del person["phone"]

# write string back as json object
new_data = json.dumps(data, indent=2)

# sorting is possible
json.dumps(data, indent=2, sort_keys=True)



# ----------using json on files----------
def __read_json_file(path):
    with open(path,"r") as file:
        d = json.load(file)
    return d

def __write_json_file(self, path): 
    with open(path,"w") as file:
        json.dump(self.stops, file)




# ----------using json on urls----------
from urllib.request import urlopen

# placeholder json api
with urlopen("https://jsonplaceholder.typicode.com/todos") as response:
    source = response.read()

data = json.loads(source)
data_str = json.dumps(data, indent=2)
# print(data_str)


# use the data
users = dict()
for item in data:
    uid = item["userId"]
    id = item["id"]
    users[id] = uid
print(users[78])