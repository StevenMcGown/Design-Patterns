from itertools import accumulate,combinations_with_replacement,product,permutations,combinations,groupby,count,cycle,repeat as r2
from timeit import repeat as r1
import operator
# Iterators are data types that can be used in a for loop

# Product
a = [1,2]
b = [3,4]

""" Calculates the cartesian product """
prod = product(a,b, r1=2) # imported as r1
print(list(prod))

""" Permutations are used for lists (order matters) """
# Permutations
a = [1,2,3,4]
perm = permutations(a,2) # 2 is the max length
print(list(perm))

""" Combinations are used for groups (order dosn't matter) """
# Combinations
a = [1,2,3,4]
comb = combinations(a,2) # length is mandatory here
print(list(comb))
comb_wr = combinations_with_replacement(a,2) # combination will include itself
print(list(comb_wr))

""" Accumulate adds (or uses specified operator) all elements in list """
# Accumulate
a = [1,2,5,3,4]
acc = accumulate(a, func=operator.mul)
print(list(acc))
acc = accumulate(a, func=max)
print(list(acc))

""" Groups items in a list by a given key - can use lambda functions """
# Group by
def smaller_than_3(x):
  return x < 3

a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
  print(key, list(value))

persons =[{'name': 'Tim', 'age': 25},{'name': 'Bob', 'age': 25},
          {'name': 'Lisa', 'age': 22},{'name': 'Ann', 'age': 21}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
  print(key, list(value))

# Count
for i in count(10):
  print(i)
  if i == 15:
    break

# Cycle
num = 0
a = [1,2,3]
for i in cycle(a):
  print(i)
  num+=1
  if num == 2: # break on condition
    break

# Repeat
a = [1,2,3]
for i in r2(1, 4): # repeat 4 times (imported as r2)
  print(i)