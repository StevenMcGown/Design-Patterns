class Employee:

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

  def fullName(self):
    return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Bob', 'Ross', 64000)
emp_2 = Employee('Alice', 'Caldwell', 62000)

print(Employee.raise_amount)
print(emp_1.raise_amount) # Accessing class attributes
print(emp_2.raise_amount) 
