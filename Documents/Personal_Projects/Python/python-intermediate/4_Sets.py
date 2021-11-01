#sets are mutable and unordered, but they do not allow duplicate elements
my_set = {1,2,3,3,2,1}
print(my_set)

print(set("Hello"))

# create empty set
my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
print(my_set)

# remove
my_set.remove(4)
print(my_set)

# discard does the same thing, although it will do nothing if it doesn't find the element
my_set.discard(5)

# pop
my_set.pop()
print(my_set)

# if in 
if 1 in my_set:
  print('yes')

#Union, intersection and differences
odds = {1,3,5,7,9,11,13,15,17}
evens = {0,2,4,6,8,10,12,14,16}
primes = {2,3,5,7,11,13,17,19,23}

u = odds.union(evens) #combines elements without duplication
print(u)

i = odds.intersection(primes)
print(i)

d = odds.difference(primes) # difference between set A and set B
print(d)

sd = odds.symmetric_difference(primes) # all of the elements that are in exactly one set
print(sd)

# update
setA = odds.copy()
setB = evens.copy()

setA.update(setB)
print(setA)

setA = odds.copy()
setB = evens.copy()

setA.intersection_update(setB) # only keeps the elements found in both sets
print(setA)

setA = odds.copy()
setB = evens.copy()

setA.difference_update(setB) # updates the set by removing the elements found in another set
print(setA)

setA = odds.copy()
setB = evens.copy()

setA.symmetric_difference_update(setB) # updates the set but only keeps the elements not found in both

# sub set, super set, disjoint sets
setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {7,8}

print(setA.issubset((setB))) # subsets mean all the elements in the first set are also in the second set
print(setB.issubset((setA)))

print(setA.issuperset((setB))) # supersets are the opposite of subsets
print(setB.issuperset((setA)))

print(setA.isdisjoint((setB))) # if both sets have no same elements
print(setA.isdisjoint((setC)))

# frozen set (immutable set)
a = frozenset([1,2,3,4])
a.add(2)