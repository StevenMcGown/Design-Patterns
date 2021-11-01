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

emp_1 = Employee('Bob', 'Ross', 64000)
emp_2 = Employee('Alice', 'Caldwell', 62000)

print(Employee.num_of_emps)

print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount) # Accessing class attributes
print(emp_2.raise_amount) 


# Important concept to understand
print("Changing class attribute 'raise amount' to 1.05")
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print("Changing class instance attribute 'raise amount' to 1.06")
emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount) 