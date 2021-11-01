from functools import reduce
"""
Used when you need a simple function only once in your code or as an argument to higher order functions
Lambda syntax -> arguments: expression
"""
add10 = lambda x: x + 10
print(add10(5))

def add10_func(x):
  return x+10
print(add10_func(5))

# Multiple args
mult = lambda x,y: x*y
print(mult(2,7))

# Lists
points2D = [(1,2),(15,1),(5,-1),(10,4)]

""" Using function """
def sort_by_y(x):
  return x[1]

points2D_sorted = sorted(points2D, key=sort_by_y)
print(points2D)
print(points2D_sorted)

""" Using lambda function """
points2D_sorted = sorted(points2D, key=lambda x: x[1]) # Sorts values according to the second index of the points2D list

print(points2D)
print(points2D_sorted)

# Map function syntax -> map(func, seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

""" You can also use this """
c = [x*2 for x in a]
print(c)

# Filter function syntax -> filter(func, seq)
a = [1,2,3,4,5]
b = filter(lambda x: x%2==0,a) # Filter even numbers
print(list(b))

""" You can also use this """
c = [x for x in a if x%2==0]
print(c)

# Reduce function syntax -> reduce(func, seq)
a = [1,2,3,4,5]

product_a = reduce(lambda x,y: x*y, a)
print(product_a)