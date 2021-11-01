# seem random but they are reproducable
import random

a = random.random()
print(a)

b = random.uniform(1,10)
print(b)

c = random.randint(1,10) # range from 1 to 10 (includes the upper bound 10)
print(c)

d = random.randrange(1,10) # does not include the upper range
print(d)

e = random.normalvariate(0, 1) #(μ, σ) picks a random normal variate
print(e)

# Pick from list
mylist = list("ABCDEFGH")
a = random.choice(mylist)
print(a)

b = random.sample(mylist, 3) #picks unique elements, never the same twice
print(b)

c = random.choices(mylist, k=3) #can pick same element three times
print(c)

d = random.shuffle(mylist)
print(mylist)

# Showing randoms are reproducable
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))


# Demonstating the secrets module. Used for security purposes as opposed to random. Secrets are not reproducable
import secrets
a = secrets.randbelow(10)
print(a)

b = secrets.randbits(4) #e.g. 1010
print(b)

c = secrets.choice(mylist)
print(c)

# Numpy for working with arrays. Uses a different generator than python's random
import numpy as np

a = np.random.rand(3) # produces a 1D array with 3 elements
print(a)

b = np.random.rand(3,3) # produces a 3D array with 3 elements
print(b)

c = np.random.randint(0,10,3) # random 1D array with 3 random integers
print(c)

d = np.random.randint(0,10,(3,4)) # random 3D array with 3 rows of 4 random integers
print(d)

print('####')

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr) # only shuffles the rows, not elements in rows
print(arr)

# Demonstrating numpy seed
np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(2)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(2)
print(np.random.rand(3,3))