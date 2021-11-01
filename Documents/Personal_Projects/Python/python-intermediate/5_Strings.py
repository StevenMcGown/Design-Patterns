from timeit import default_timer as timer

my_string = """Hello \
  world"""
print(my_string)

# substring
print(my_string[0:5])
print(my_string[::2])

name = "Tom"

print(my_string[0:6] + name)

for i in "Hello":
  print(i)

# remove whitespace
my_string = '   Hello World    '
my_string = my_string.strip()
print(my_string)

# conversion
print(my_string.upper())
print(my_string.lower())

# check
print(my_string.startswith("Hello"))
print(my_string.endswith("World"))

# find
print(my_string.find("o"))
print(my_string.find("2"))
print(my_string.count("l"))

# replace
print(my_string.replace('World', 'Universe'))

# convert string to a list
my_string = 'how are you doing'
my_list = my_string.split() # default is a space
print(my_list)

# joining 
new_string = '-'.join(my_list)
print(new_string)

my_list = ['a'] * 1000000

""" bad code """
start = timer()
my_string = ''
for i in my_list:
  my_string += i
stop = timer()
badtime= stop-start

""" good code """
start = timer()
my_string = ''.join(my_list)
stop = timer()

goodtime = stop-start
percent = (goodtime/badtime) * 10000
print("The good method is %.2f" % percent + "% faster")
print("Bad time: %.4f" % badtime)
print("Good time: %.4f" % goodtime)

# format strings
""" old methods for formatting strings """
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 123.456
my_string = "the variable is %d" % var
print(my_string)
my_string = "the variable is %.2f" % var
print(my_string)

var1 = 3.1415
var2 = 96535
my_string = "first variable is {:.2f} and second is {:d}".format(var1,var2)
print(my_string)

""" new methods for formatting strings since python 3.16 """
var1 = 3.1415
var2 = 96535
my_string = f"new formatted variables are {var1*2} and {var2}"
print(my_string)