# Positional Arguments
# Order matters when it comes to positional arguments

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# Multiple Function Calls

# describe_pet('horse', 'roach')
# describe_pet('direwolf', 'ghost')


# Keyword Arguments
# Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.
# describe_pet(animal_type="dragon", pet_name="azymondias")
# describe_pet(pet_name="hootsie", animal_type="owlbear",)

# Default Values
# default values allow you to prepopulate parameters with a default value/argument, the default values can be overriden however if provided with a different argument when called

def describe_pet( pet_name, animal_type = "dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="willie")

# To override default values however you can simply do the following
describe_pet(pet_name="harry", animal_type='hamster')

# A dog named Willie
# describe_pet('willie')
# describe_pet(pet_name='willie')

# A hamster named harry
# describe_pet('harry','hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

