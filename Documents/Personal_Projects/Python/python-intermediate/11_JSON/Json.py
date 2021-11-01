import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True) # configure dictionary to json parsing parameters
#print(personJSON)

# Writing to file
with open('./11_JSON/json_files/person.json', 'w') as file:
  json.dump(person, file, indent=4)

# Load in python format
person = json.loads(personJSON) #notice load(s)
print(person)

# Read from file
with open('./11_JSON/json_files/person.json', 'r') as file:
  person = json.load(file) # notice loa(d)
  print(person)
