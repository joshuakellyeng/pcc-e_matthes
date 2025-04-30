# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepper', 'extra cheese')

# Mixing Positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, the
# parameter that accepts an arbitrary number of arguments must be placed
# last in the function definition.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')
# You’ll often see the generic parameter name *args, which collects arbitrary positional
# arguments like this.