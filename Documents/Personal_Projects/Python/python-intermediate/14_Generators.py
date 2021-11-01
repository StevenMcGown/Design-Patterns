# Return an object that can be iterteated over. Generate items one at a time and only when you ask for it.
# They are much more memory efficient when working with large datasets.

def mygenerator():
  # yield is similar to return
  yield 1
  yield 3
  yield 2


# Iterate through values\
g = mygenerator()
for i in g:
  print(i)

# get values one at a time with next()
g = mygenerator()
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)

# Raises StopIteration exception
# print(value)
# value = next(g)

#get sum
g = mygenerator()
print(sum(g))

#get sorted
g = mygenerator()
print(sorted(g))

#execution of a generator function
def countdown(num):
  print('Starting')
  while num > 0:
    yield num
    num -= 1

cd = countdown(3)

value = next(cd)
print(value)

print(next(cd))
print(next(cd))

# Generators are memory efficient

import sys

#Usually what you would do to generate a list of numbers is...
def firstn(n):
  nums = [] # all of the numbers are stored in this list, which takes a lot of memory
  num = 0
  while num < n:
    nums.append(num)
    num +=1
  return nums

print(sys.getsizeof(firstn(1000000))) # gets size in bytes (going to be larger)

#Instead we can use generators to save memory
def firstn_generator(n):
  num = 0
  while num < n:
    yield num
    num+=1

print(sys.getsizeof(firstn_generator(100000))) # gets size in bytes (going to be smaller)



# Generator fibonacci sequence

def fibonacci(limit):
  # 0 1 1 2 3 5 etc...
  a,b = 0,1
  while a < limit:
    yield a
    a,b = b,a+b

fib = fibonacci(100)

for i in fib:
  print(i)


# Typical way to generate even numbers in a list
mylist = [i for i in range(1000) if i % 2 == 0] # all the even elements from 0 to 9
print(sys.getsizeof(mylist))

# Simple generator expression saves a lot of memory
mygenerator = (i for i in range(1000) if i % 2 == 0) # all the even elements from 0 to 9
print(sys.getsizeof(mygenerator))