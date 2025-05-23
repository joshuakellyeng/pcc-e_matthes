# Working with Classes and Instances
# The Car Class

# We include a module-level docstring that briefly describes the content of this module.
"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # Setting a Default Value for an Attribute
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    # Modifying an Attribute’s Value Through a Method
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        Reject the operation if it attempts submit a negative number.
        """
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
            
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# # Modifying Attribute Values
# # my_new_car.odometer_reading = 23

# my_new_car.update_odometer(26)
# my_new_car.read_odometer()

# my_used_car = Car('subaru', 'outback', 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(-50)
# my_used_car.read_odometer()



