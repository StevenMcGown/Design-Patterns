from collections import Counter,namedtuple,OrderedDict,defaultdict,deque

""" For special container data types """
# Counter
a = "aaaaabbbbccc"
my_Counter = Counter(a)
print(my_Counter.items())
print(my_Counter.keys())
print(my_Counter.values())

print(my_Counter.most_common(2)) # returns a list of tuples of the number of most common element
print(my_Counter.most_common(2)[0][0])
print(list(my_Counter.elements()))

# named tuples
Point = namedtuple('Point', 'x,y')
pt = Point(1,-5)
print(pt.x, pt.y)

# Ordered dict
""" Python 3.7 allows ordered all dictionaries to be ordered """
ordered_dict = OrderedDict()
ordered_dict['z'] = 26
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

# default dict
""" Will have a default value if the key has not been set """
d = defaultdict(list) # default type list
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['a'])
print(d['d'])

# deque (double ended queue)
""" Can be used to add or remove elements from both ends """
d = deque()

d.append(1)
d.append(2)
print(d)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d.extend([4,5,6])
print(d)

d.extendleft([1,2,3])
print(d)

d.rotate(2)
print(d)
d.rotate(-2)
print(d)