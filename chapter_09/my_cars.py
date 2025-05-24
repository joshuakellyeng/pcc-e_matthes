# Importing Multiple Classes from a Module
# from car import Car, ElectricCar

# Importing entire module
# import car

# Importing a Module into a Module
# from car import Car
# from electric_car import ElectricCar

# Using Aliases
# from electric_car import ElectricCar as EC
import electric_car as ec
import car as c
# my_mustang = Car('ford', 'mustang', 2024)

# my_mustang = Car('ford', 'mustang', 2024)
my_mustang = c.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

