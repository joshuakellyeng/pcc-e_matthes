# Creating and Using a Class

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Making an Instance from a Class

my_dog = Dog('Willie', 6)
# Creating Multiple Instances
# You can create as many instances from a class as you need. Let’s create a
# second dog called your_dog:
your_dog = Dog('Lucy', 3)

# Accessing Attributes - use dot notation to access attributes of an instance.
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()