from classes import Car, ElectricCar, Person, Variable_Species

car1=Car(brand='Honda',model='Vezel',year=2000)
car2=Car(brand='Audi',model='X',year=2000)
car3=Car(brand='Mercedez',model='C200',year=2000)
print(car1.brand,car1.model,car1.year)
electric_car1=ElectricCar(brand='Cheverolet',model='RX',year=2000,battery_capacity=1200)
electric_car2=ElectricCar(brand='Tesla',model='WX',year=2025,battery_capacity=1600)
electric_car3=ElectricCar(brand='Hyundai',model='Wex',year=2009,battery_capacity=1298)
electric_car4=ElectricCar(brand='Mitsubishi',model='BN',year=2023,battery_capacity=1890)
print(car1.display_info())
print(car2.display_info())
print(electric_car1.display_info())
print(electric_car2.battery_info())
print(electric_car3.display_info())
print(electric_car4.battery_info())
p1=Person(name='Alice',age=18)
print(p1.introduce())
print(p1.introduce())


