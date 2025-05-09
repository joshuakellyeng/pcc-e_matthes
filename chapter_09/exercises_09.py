# 9.1 Restaurants

class Restaurant:
    """A simple attempt to model a restaurant"""
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

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# 9.2 Three Restaurants
first_restaurant = Restaurant("harry's daughter", 'jamaican')
second_restaurant = Restaurant("mini bar", 'spanish')
third_restaurant = Restaurant('french toast', 'french southern fusion')

first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()

# 9.3 Users

class User:
    """A simple attempt to try and model a user."""
    def __init__(self, first_name, last_name, class_type, country_of_origin):
        """Initializing user and user data"""
        self.first_name = first_name
        self.last_name = last_name
        self.class_type = class_type
        self.country_of_origin = country_of_origin
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Class Type: {self.class_type.title()}")
        print(f"Place of Origin: {self.country_of_origin.title()}")

    def greet_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} the {self.class_type.title()}, welcome.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

the_monk = User('beauregard', 'lionette', 'monk of the cobalt soul', 'kamordah')
the_wizard = User('caleb', 'widogast', 'wizard of transmutation', 'blumenthal')
the_paladin = User('fjord', 'tusktooth', 'paladin of the open sea', 'port demali')
the_trickster = User('jester', 'lavorre', 'cleric of trickery', 'nicodranas')
the_cleric = User('cadeuces', 'clay', 'cleric of the grave', 'blooming grove')
the_rogue = User('veth', 'brenatto', 'arcane trickster', 'felderwyn village')
the_barbarian = User('yasha', 'nydoorin', 'barbarian of the zealot', 'xhorhas')

the_monk.describe_user()
the_monk.greet_user()
print("\n")

the_wizard.describe_user()
the_wizard.greet_user()
print("\n")

the_paladin.describe_user()
the_paladin.greet_user()
print("\n")

the_trickster.describe_user()
the_trickster.greet_user()
print("\n")

the_cleric.describe_user()
the_cleric.greet_user()
print("\n")

the_rogue.describe_user()
the_rogue.greet_user()
print("\n")

the_barbarian.describe_user()
the_barbarian.greet_user()


# 9.4 Number Served

restaurant = Restaurant('rumba cubana', 'cuban')
restaurant.describe_restaurant()
print("Numbers Served:", restaurant.number_served)

# restaurant.number_served = 25_000
restaurant.set_number_served(1001)
print("Numbers Served:", restaurant.number_served)

restaurant.increment_number_served(336)
print("Numbers Served:", restaurant.number_served)

# 9.5 Login Attempts

the_dunamancer =User('essek', 'thelyss', 'wizard of dunamancy', 'xhorhas')
print("Starting Login Attempts:",the_dunamancer.login_attempts)

the_dunamancer.increment_login_attempts()
the_dunamancer.increment_login_attempts()
the_dunamancer.increment_login_attempts()
print("Current Login Attempts:",the_dunamancer.login_attempts)

the_dunamancer.reset_login_attempts()
print("Final Login Attempts:",the_dunamancer.login_attempts)
