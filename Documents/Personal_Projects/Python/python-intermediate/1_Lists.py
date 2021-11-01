# Lists are ordered, mutable, and allow duplicate elements
print("Lists are ordered, mutable, and allow duplicate elements")

list1 = ["a", "b", "c", 1, 2, 3]
print(list1)

# empty list
print("empty list")

emptyList = list()
print(emptyList)

# access element
print("access element")

item = list1[1]
print(item)

# last element in the list
print("last element in the list")

print(list1[-1])

# print all elements
print("print all elements")

for x in list1:
  print(x)

# use the length of the list
print("use the length of the list")

for x in range(len(list1)):
  print(list1[x])

# check if item is in list
print("check if item is in list")

if "c" in list1:
  print("yes")
else:
  print("no")

# append to empty list
print("append to empty list")

emptyList.append("red")
emptyList.append("green")
emptyList.append("blue")
print(emptyList)

# insert
print("insert")

emptyList.insert(1, "orange")
emptyList.insert(2, "yellow")
emptyList.insert(5, "violet")
print(emptyList)

# remove
print("remove")

emptyList.remove("green")
emptyList.remove("orange")
emptyList.remove("violet")
print(emptyList)

# pop
print("pop")

emptyList.pop()
print(emptyList)
emptyList.pop()
print(emptyList)
emptyList.pop()
print(emptyList)

for i in range(10):
  emptyList.append(i)

print(emptyList)

# reverse list
print("reverse list")

emptyList.reverse()
print(emptyList)

# clear
print("clear")

emptyList.clear()
print(emptyList)

# sort
print("sort")

emptyList = [4,8,2,7,5]
#emptyList.sort()
print(emptyList)

new_list = sorted(emptyList)
print(new_list)

# new list with n elements
print("new list with n elements")

new_list = [5] * 6
print(new_list)

# put lists together
print("Put lists together")

list2 = list1 + new_list
print(list2)

# slicing

print("Slicing")

list1.clear()
for i in range(10):
  list1.append(i)

a = list1[0:5] #from 0 to 5th element
print(a)

b = list1[5:] #after fifth element
print(b)

c = list1[:5] #up to fifth element
print(c)

d = list1[::2] #every two items
print(d)

e = list1[::-1] #another way to reverse list
print(e)

# Careful copying lists

print("Pass by value vs. pass by reference")
list_org = ["banana", "cherry", "apple"]

"""this assignment changes assigns the same memory address"""
list_cpy = list_org 
"""these 3 assignments pass by reference (these 3 do the same thing)"""
list_cpy = list_org.copy() 
list_cpy = list(list_org)
list_cpy = list_org[:]

list_cpy.append("blueberry")

print(list_org)
print(list_cpy)

# Square each element
print("Square each element")
squares = []
for i in range(10):
  squares.append(i)

b = [i*i for i in squares]
print(b)
