import json

class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

user1 = User('Max', 27)

# Takes an object and checks if object is an instance of a class
def encode_user(object):
  if isinstance(object, User): # object type user
    return {'name': object.name, 'age': object.age, object.__class__.__name__: True} # checks for class name
  else:
    raise TypeError('Object of type User is not JSON serializable')

userJSON1 = json.dumps(user1, default=encode_user) #encodes the user object
print(userJSON1)

### Another way ###

from json import JSONEncoder


class UserEncoder(JSONEncoder):
  def default(self, object):
      if isinstance(object, User):  # object type user
        return {'name': object.name, 'age': object.age, object.__class__.__name__: True} # checks for class name
      return JSONEncoder.default(self, object)

user2 = User('Bob', 23)

userJSON2 = UserEncoder().encode(user2)
print(userJSON2)

# Decode object back to python dict object

print(type(user1))
user1 = json.loads(userJSON1)
print(type(user1))

def decode_user(dictionary):
  if User.__name__ in dictionary:
    return User(name=dictionary['name'], age=['age'])
  return dictionary # otherwise decode into dictionary

user1 = json.loads(userJSON1, object_hook=decode_user) # this will decode back into user object
print(type(user1))
print(user1.name) # you can now use user variables
