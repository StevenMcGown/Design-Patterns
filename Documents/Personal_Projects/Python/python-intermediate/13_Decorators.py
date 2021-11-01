# A decorator is a function that takes another function as an argument and extends the
# behavior of the function without explicity modifying it
import functools

#### Function decorators example 1 ####
def my_decorator(func):

  @functools.wraps(func) # preserves the information of the used function
  # wraps the function
  def wrapper(*args, **kwargs): # use as many arguments and keyword arguments as you want
    # Do...
    result=func(*args, **kwargs)
    # Do...
    return result
  return wrapper

#Decorator gives the function new functionality
@my_decorator
def add5(x):
  return x+5

result = add5(10)
print(result)

#print(help(add5))
#print(add5.__name__)


#### Function Decorator Example 2 ####

def repeat(num_times):

  def decorator_repeat(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

      for _ in range(num_times):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat

# Give parameters to a decorator
@repeat(num_times=3)
def greet(name):
  print(f'Hello {name}')

greet('Alex')

#### Nested decorators ####

def start_end_decorator(func):

  @functools.wraps(func) # preserves the information of the used function
  # wraps the function
  def wrapper(*args, **kwargs): # use as many arguments and keyword arguments as you want
    print('Start')
    result=func(*args, **kwargs)
    print('End')
    return result
  return wrapper

# Extracts the name, the arguments and keyword arguments and executes the function 
# prints the information of the function of the return value
def debug(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

# Multiple decorators on functions are executed in the order in which they are listed
@debug
@start_end_decorator
def say_hello(name):
  greeting = f'Hello {name}'
  print(greeting)
  return greeting

say_hello('Bob')

#### Class Decorator ####
# Do the same thing as function decorators but they are typically used to maintain and
# update a state

class CountCalls:

  def __init__(self, func):
    self.func = func 
    self.num_calls = 0 #Keep track of the number of calls

  # Allows you to execute a object of this class just like a function
  def __call__(self, *args, **kwargs):
    self.num_calls += 1
    print(f'This is executed {self.num_calls} times')
    return self.func(*args,**kwargs)
  
@CountCalls
def say_hello():
  print('Hello')

say_hello()
say_hello()
