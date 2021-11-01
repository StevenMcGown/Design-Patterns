import datetime

class Employee:

  num_of_emps = 0
  raise_amount = 1.04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

    Employee.num_of_emps += 1

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

  @classmethod # Need this to access class variables
  def set_raise_amt(cls, amount):
    cls.raise_amount = amount

  #Allows you to pass in a string and make an employee from it
  @classmethod
  def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

  # You might use static methods if you don't acess the 
  @staticmethod
  def is_workday(day):
    if day.weekday() >= 5:
      return False
    return True

emp_1 = Employee('Bob', 'Ross', 64000)
emp_2 = Employee('Alice', 'Caldwell', 62000)

print(Employee.raise_amount)
print(emp_1.raise_amount) # Accessing class attributes
print(emp_2.raise_amount) 

#These do the same thing
Employee.set_raise_amt(1.05)
emp_1.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount) # Accessing class attributes
print(emp_2.raise_amount)

#########################################

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.first)
my_date = datetime.date(2021, 10, 31)

print(Employee.is_workday(my_date))