from user_module import User


# 9.1 Restaurants

class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """A method that describes a restaurant"""
        print(f"Our restaurant is called {self.restaurant_name.title()}.")
        print(f"We specialize in {self.cuisine_type.title()} cuisine.\n")

    def open_restaurant(self):
        """A method that simulates a restaurant opening"""
        print(f"{self.restaurant_name.title()} is now open for business!")

    def set_number_served(self,number_served):
        """A method to set the amount of patrons served."""
        self.number_served = number_served

    def increment_number_served(self, number):
        """A method to increase the amount of patrons served."""
        self.number_served += number


my_restaurant = Restaurant("saigon bistro", 'vietnamese' )

# print(my_restaurant.restaurant_name)
# print(my_restaurant.cuisine_type)
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# 9.2 Three Restaurants
first_restaurant = Restaurant("harry's daughter", 'jamaican')
second_restaurant = Restaurant("mini bar", 'spanish')
third_restaurant = Restaurant('french toast', 'french southern fusion')

# first_restaurant.describe_restaurant()
# second_restaurant.describe_restaurant()
# third_restaurant.describe_restaurant()

# 9.3 Users

the_monk = User('beauregard', 'lionette', 'monk of the cobalt soul', 'kamordah')
the_wizard = User('caleb', 'widogast', 'wizard of transmutation', 'blumenthal')
the_paladin = User('fjord', 'tusktooth', 'paladin of the open sea', 'port demali')
the_trickster = User('jester', 'lavorre', 'cleric of trickery', 'nicodranas')
the_cleric = User('cadeuces', 'clay', 'cleric of the grave', 'blooming grove')
the_rogue = User('veth', 'brenatto', 'arcane trickster', 'felderwyn village')
the_barbarian = User('yasha', 'nydoorin', 'barbarian of the zealot', 'xhorhas')

# the_monk.describe_user()
# the_monk.greet_user()
# print("\n")

# the_wizard.describe_user()
# the_wizard.greet_user()
# print("\n")

# the_paladin.describe_user()
# the_paladin.greet_user()
# print("\n")

# the_trickster.describe_user()
# the_trickster.greet_user()
# print("\n")

# the_cleric.describe_user()
# the_cleric.greet_user()
# print("\n")

# the_rogue.describe_user()
# the_rogue.greet_user()
# print("\n")

# the_barbarian.describe_user()
# the_barbarian.greet_user()


# 9.4 Number Served

restaurant = Restaurant('rumba cubana', 'cuban')
# restaurant.describe_restaurant()
# print("Numbers Served:", restaurant.number_served)

# restaurant.number_served = 25_000
# restaurant.set_number_served(1001)
# print("Numbers Served:", restaurant.number_served)

# restaurant.increment_number_served(336)
# print("Numbers Served:", restaurant.number_served)

# 9.5 Login Attempts

the_dunamancer =User('essek', 'thelyss', 'wizard of dunamancy', 'xhorhas')
# print("Starting Login Attempts:",the_dunamancer.login_attempts)

the_dunamancer.increment_login_attempts()
the_dunamancer.increment_login_attempts()
the_dunamancer.increment_login_attempts()
# print("Current Login Attempts:",the_dunamancer.login_attempts)

the_dunamancer.reset_login_attempts()
# print("Final Login Attempts:",the_dunamancer.login_attempts)

# 9.6 Ice Cream Stand

class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand."""
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """A simple method that prints all flavors available."""
        print("\nHere's a list of our current available flavors: ")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


torico = IceCreamStand('torico')
torico.flavors =['pistachio', 'vanilla', 'strawberry', 'chocolate', 'cookies and cream']

# torico.describe_restaurant()
# torico.show_flavors()

# 9.7 Admin

class Admin(User):
    """A user with administrative privileges."""
    def __init__(self, first_name, last_name, class_type, country_of_origin):
        super().__init__(first_name, last_name, class_type, country_of_origin)
        self.privileges = Privileges()


# m_tealeaf = Admin('mollymauk', 'tealeaf', 'bloodhunter', 'trostenwald')
# m_tealeaf.privileges = ['can add post', 'can delete post', 'can ban user', 'can unban user', 'can lock threads', 'can unlock threads', 'can pin post', 'can unpin post']
# m_tealeaf.show_privileges()

# 9.8 Privileges
class Privileges:
    """A simple attemp to model admin privileges."""
    def __init__(self, privileges =[]):
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print(f"Admin Privilages: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f'- {privilege.title()}')
        else:
            print("User has no privileges.")

k_mitnick = Admin('kevin', 'mitnick', 'artificer', 'united states')
k_mitnick_priveleges = ['ham radios', 'social engineering', 'phone phreaking']
k_mitnick.privileges.privileges = k_mitnick_priveleges

# k_mitnick.describe_user()
# k_mitnick.privileges.show_privileges()

# 9.9 Battery Upgrade

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
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

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size == 40:
            self.battery_size = 65
            print("Upgraded the battery to 65 kWh.")
        else:
            print("The battery is already upgraded.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    # Defining Attributes and Methods for the Child Class
    # def describe_battery(self):
    #     """Print a statement describing the battery size."""
    #     print(f"This car has a {self.battery_size}-kWh battery.")

my_kona = ElectricCar('hyundai', 'kona', 2025)

# print("\n")
# print(my_kona.get_descriptive_name())
# my_kona.battery.describe_battery()
# my_kona.battery.get_range()

# print(my_kona.get_descriptive_name())
# my_kona.battery.upgrade_battery()
# my_kona.battery.describe_battery()
# my_kona.battery.get_range()

# 9.13 Dice
from random import randint, choice

class Die:

    """A simple attempt at modeling a Die Roll"""
    def __init__(self, die_size=6):
        self.die_size = die_size

    def roll_die(self):
        result = randint(1, self.die_size)
        print(f"D{self.die_size}: {result}")

d20 = Die(20)
d10 = Die(10)

# d20.roll_die()
# d10.roll_die()
# print("\n")
# d20.roll_die()
# d10.roll_die()
# print("\n")
# d20.roll_die()
# d10.roll_die()
# print("\n")
# d20.roll_die()
# d10.roll_die()
# print("\n")
# d20.roll_die()
# d10.roll_die()

# 9.14 Lottery

lottery = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E']

def ticket_generator(lottery):
    winning_ticket = ''
    for x in range(4):
        char = choice(lottery)
        winning_ticket+=str(char)
    # print(f"Ticket Number: {winning_ticket} is today's WINNER!")
    return winning_ticket

# ticket_generator(lottery)

# 9.15 Lottery Analysis

my_ticket = ticket_generator(lottery)
# print(my_ticket)

def lottery_analysis(ticket_value, lottery):
    winning_ticket = ''
    count = 0
    while ticket_value != winning_ticket:
        winning_ticket = ticket_generator(lottery)
        count += 1
    message = f"It took {count} times for your ticket: {ticket_value} to match the winning ticket: {winning_ticket}!"
    return message

print(lottery_analysis(my_ticket,lottery))

# 9.16 Python Module of the Week
# https://pymotw.com/3/random/index.html