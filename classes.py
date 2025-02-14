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

    def __init__(self, name, age):
        self.name = name
        self.age = age


    # def __call__(self):
    #     self.age = age
    #     return f'{self.name} updated age: {self.age} years old'
    def introduce(self):
        self.age += 1
        return f'Hi, my name is {self.name} and I am {self.age} years old.'


        return f'I am {self.age} years old.'


class Variable_Species(Person):
    def __init__(self, name, age,human):
        super().__init__(name, age)
        self.variable_species = human
