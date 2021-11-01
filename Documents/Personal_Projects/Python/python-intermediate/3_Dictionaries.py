my_dict = {"name": "Max", "age": 28, "city": "Beaufort"}
print(my_dict)

my_dict = dict(name="Max", age=28, city="Beaufort")
print(my_dict)

# access values
print(my_dict["name"])

# change values
my_dict["age"] = 25
print(my_dict)

# delete values
del my_dict["city"]
print(my_dict)

my_dict.popitem()
print(my_dict)

# check if key is in dictionary
if "name" in my_dict:
    print("yes")

try:
    print(my_dict["lastname"])
except:
    print("error")

# loop through dictionary
my_dict = {"name": "Max", "age": 28, "city": "Beaufort"}
print(my_dict)

for key in my_dict.keys():
  print(key)

for value in my_dict.values():
  print(value)

for key, value in my_dict.items():
  print(key, value)

# Be careful copying dictionaries, same deal as with lists

#this assignment changes assigns the same memory address
dict_cpy = my_dict
dict_cpy["name"] = "Maxwell"
print(my_dict)
print(dict_cpy)

#these 3 assignments pass by reference (they do the same thing)
dict_cpy = my_dict.copy() 
dict_cpy = dict(my_dict)
dict_cpy["name"] = "Max"

print(my_dict)
print(dict_cpy)

# Merge two dictionaries
my_dict = {"name": "Max", "age": 28, "email": "max@gmail.com"}
my_dict_2 = dict(name="Mary", age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

print(my_dict[3])

my_tuple = (8,7)
my_dict = {my_tuple: 15}

print(my_dict)

