# 7.1 Rental Car

# car = input("Thanks for choosing Atom Rentals! \nWhat car would you like to rent today? \n")

# print(f"\nLet me see if I can find you a {car}.")

# 7.2 Restaurant Seating

# num_of_guests = input("Welcome to The Prancing Pony \nHow many folks are in your party? ")

# num_of_guests = int(num_of_guests)

# if num_of_guests > 8:
#     print("\nThere is about a 20 minute wait for a table at the moment.")
# else:
#     print("\nWonderful! I have just the table for your group! Please follow me.")

# 7.3 Multiples of Ten

# mult_of_ten = input("Please enter a number, \nand I will tell you if it is a multiple of 10 or not. \n")

# mult_of_ten = int(mult_of_ten)

# if mult_of_ten % 10 == 0:
#     print(f"\n{mult_of_ten} IS a multiple of 10.")
# else:
#     print(f"\n{mult_of_ten} IS NOT a multiple of 10.")

# 7.4 Pizza Toppings

# pizza_prompt = "What topping would you like on your pizza? \n"
# pizza_promt += "Enter 'quit' when you are finished: \n"
# active = True
# while active:
#     answer = input(pizza_prompt)

#     if answer == 'quit':
#         active = False
#     else:
#         print(f"\nAwesome! Adding {answer} to your pizza!\n")

# 7.5 Movie TIckets

# movie_prompt = f"Welcome to Atom Cinema!"
# movie_prompt+= f"Please provide your age so that we can let you know the cost of your ticket: \n"

# active = True
# while True:
#     ticket = 0
#     age = input(movie_prompt)
#  
#     if age == 'quit':
#       break  
#     age = int(age)

#     if age < 3:
#         ticket = 0
#     elif age < 13:
#         ticket = 10
#     else:
#         ticket = 15
    
#     if ticket == 0:
#         print(f"The ticket is FREE! Enjoy the show!")
#     else:
#         print(f"The price is {ticket} for your ticket! Enjoy the show!")

# 7.6 Three Exits
# a. use conditional test in while statement to stop loop

# pizza_intro = "\nWelcome to Planet Pizza! Where we exclusive make extra large pies! \n"
# pizza_intro += "Please let me know what topping you'd like on your pie! \n"
# pizza_intro += "(Enter 'quit' to terminate the program.) \n"


# answer = ''
# while answer != 'quit':
#     answer = input(pizza_intro)
#     if answer != 'quit':
#         print(f"\nWonderful choice! We'll add {answer} to your pie!\n")  
    


# b. use an active variable to control how long the loop runs.

# movie_prompt = f"\nWelcome to Atom Cinema!"
# movie_prompt+= f"\nPlease provide your age so that we can let you know the cost of your ticket: \n"
# movie_prompt+= f"(Enter 'quit' to terminate the program)\n"

# active = True
# while active:
#     ticket = 0
#     age = input(movie_prompt)

#     if age == 'quit':
#         active = False
#     else:
#         age = int(age)
#         if age < 3:
#             ticket = 0
#         elif age < 13:
#             ticket = 10
#         else:
#             ticket = 15

#         if ticket == 0:
#             print(f"\nThe ticket is FREE! Enjoy the show!")
#         else:
#             print(f"\nThe price for your ticket is ${ticket}! Enjoy the show!")





# c. use a break statement to exit the loop when the user enters a 'quit' value.

# pizza_prompt = "What topping would you like on your pizza? \n"
# pizza_prompt += "(Please enter 'quit' to terminate the program.) \n"

# while pizza_prompt != 'quit':
#     answer = input(pizza_prompt)
#     if answer == 'quit':
#         break
#     else:
#         print(f"\nAwesome! Adding {answer} to your pizza!\n")

# 7.7 Infinity

# This creates an infinite loop as the value of x never changes

# message = 'Hello World!'
# x = 1
# while x < 5:
#     print(message)

# 7.8 Deli

# sandwich_orders = ['BLT', 'reuben', 'bahn mi', 'cuban', 'philly cheesteak']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"Order up! The {current_sandwich.title()} sandwich is ready!")
#     finished_sandwiches.append(current_sandwich)

# 7.9 No Pastrami

# sandwich_orders = ['BLT', 'pastrami', 'reuben', 'bahn mi', 'pastrami', 'cuban', 'philly cheesteak', 'pastrami']
# finished_sandwiches = []

# print("Sorry! We are currently out of pastrami.")

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print("\n")

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"Order up! The {current_sandwich.title()} sandwich is in the works!")
#     finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#     print(f"The {sandwich.title()} sandwich is ready!")


# 7.10 Dream Vacation
dream_vacations = {}

vacations_active = True
while vacations_active:
    name = input("What's your name? ")
    location = input("f you could visit one place in the world, where would you go? ")

    dream_vacations[name] = location

    repeat = input("Is there someone else who would like to submit their answer? ( yes/ no ) \n")
    if repeat == 'no':
        vacations_active = False
print("--- Poll Results ---")
for person, location in dream_vacations.items():
    print(f"{person.title()} would like to vacation in {location.title()}.")