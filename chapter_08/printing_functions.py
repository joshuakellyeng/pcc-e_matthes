# 8.15 Printing Models Exercise
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    # Display all completed models.
    print("\nThe following models have been printed:")  
    for completed_model in completed_models:
        print(completed_model)  
    




