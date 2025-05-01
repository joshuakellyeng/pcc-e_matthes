import printing_functions as pf

# Modifying Lists in a Function
# Start with some designs that need to be printed.

unprinted_designs = ['phone case','robot pendent', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left
# Move each design to completed_models after printing


# def print_models(unprinted_designs, completed_models):
#     """Simulate printing each design, until none are left."""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing Model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     # Display all completed models.
#     print("\nThe following models have been printed:")  
#     for completed_model in completed_models:
#         print(completed_model)  
    

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# Preventing a Function from Modifying a List
# The slice notation [:] makes a copy of the list to send to the function.
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)

pf.print_models(unprinted_designs[:], completed_models)
pf.show_completed_models(completed_models)
print(unprinted_designs)
print(completed_models)
