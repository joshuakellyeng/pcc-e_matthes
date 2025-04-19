# Positional Arguments
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('horse', 'roach')
# describe_pet('direwolf', 'ghost')


# Keyword Arguments
# Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.
# describe_pet(animal_type="dragon", pet_name="azymondias")
# describe_pet(pet_name="hootsie", animal_type="owlbear",)

# Default Values

def describe_pet( pet_name, animal_type = "dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cody')
# describe_pet('direwolf', 'ghost')
