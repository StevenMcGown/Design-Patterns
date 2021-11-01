# Errors and exceptions
""" 
Even if a function is syntactically correct, it still may throw an error
This is called an exception

a = 5 + '10' # type error
print(a)

import somemodule # import error

b = c # name error (name does not exist)

f = open('somefile.txt') # file not found error

a = [1,2,3,4]
a.remove(5) # value error (value not found)
a[5] # Index error

my_dict = {'name': 'max'}
my_dict['age'] # Key error 

"""

x=-5

""" These will prevent code from executing further
#if x < 0:
#  raise Exception('x should be positive')

#assert(x >= 0), 'x is not positive' # will raise an assertion error
"""

try:
  a = 5 / 1
  #b = a + '1'
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print('everything is fine')
finally: # runs always even if there is an exception (cleanup operations)
  print('cleaning up')

# Exceptions in classes
class ValueTooHighError(Exception):
  pass

class ValueTooLowError(Exception):
  def __init__(self, message, value): #custom init method
      self.message = message
      self.value = value


def test_value(x):
  if x > 100:
    raise ValueTooHighError('value is too high')
  if x < 5:
    raise ValueTooLowError('value is too low', x)

try:
  test_value(4)
except ValueTooHighError as e:
  print(e)
except ValueTooLowError as e:
  print(e.message, e.value)