# 9.1 Restaurants

class Restaurant:
    """A simple attempt to model a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Our restaurant is called {self.restaurant_name.title()}.")
        print(f"We specialize in {self.cuisine_type.title()} cuisine.\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open for business!")


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