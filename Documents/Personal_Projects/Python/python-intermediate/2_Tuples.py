import sys,timeit
# Tuples are ordered and immutable, for objects that belong together
my_tuple = ("Max", 28, "Austin")
print(my_tuple)

#if you want a tuple with one element:
my_tuple = ("Max")
print(type(my_tuple))
my_tuple = ("Max",)
print(type(my_tuple))

# create a tuple from a list
my_list = ["Max", 28, "Austin"]
my_tuple = tuple(my_list)
print(my_tuple)

# create a list from a tuple
my_list = list(my_tuple)

print(my_list)

#index tuple
print(my_tuple[1])
print(my_tuple[-1])

# if in 
if "Max" in my_tuple:
  print("yes")

# count number of elements in the tuple
my_tuple = ('a','p','p','l','e')
print(my_tuple.count('p'))
print(my_tuple.count('l'))
print(my_tuple.count('e'))

# find the first index of element in tuple
print(my_tuple.index('p'))
print(my_tuple.index('l'))

# slicing
a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5] # from index 2 to 5, last nidex not included
print(b)

# Packing / unpacking tuples
my_tuple = "Max", 28, "Austin"
name, age, location = my_tuple
print(name)
print(age)
print(location)

#name, age = my_tuple # wrong number of elements to unpack

my_tuple = (0,1,2,3,4)
i1, *i2, i3 = my_tuple # puts elements in a list in a tuple
print(i1)
print(i2)
print(i3)

# Because tuples are immutable, python can optimize tuples
my_list = [0,1,2,"hello", True]
my_tuple = (0,1,2,"hello", True)
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))