class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        # print(self.make, self.model, self.year)
        return f'The car is {self.brand} {self.model} and year {self.year}'
class ElectricCar(Car):
    def __init__(self, brand, model, year,battery_capacity):
        super().__init__(brand,model,year,)
        self.battery_capacity = battery_capacity
    def battery_info(self):
        return f'The car is {self.battery_capacity}kWH battery capacity'
class Person:
    def __init__(self,name,age):
      self.name = name
      self.age = age
    def introduce(self):
        return f'Hello, my name is {self.name} I am {self.age} years old'
class Species(Person):
   Species="Human"

   def __init__(self, name, age,species):
       super().__init__(name,age)
       print(f'Hello my name is {self.name} and I am {self.age} years old. I am {self.Species}')

class Employee:
    def __init__(self, name, age, salary):
            self.name = name
            self.age = age
            self.salary = salary
    def employee_salary(self):
            employee_salary = self.salary + 10000
            return employee_salary
class FullTimeEmployee(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.hours_worked = hours_worked
    def employee_salary(self):
        employee_salary = self.salary * self.hours_worked + 10000
        return employee_salary
class PartTimeEmployee(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name,age,salary)
        self.hours_worked = hours_worked
    def employee_salary(self):
        employee_salary = self.salary * self.hours_worked - 5000
        return employee_salary