# Using break to Exit a Loop

prompt = "\nPlease enter the name of a city uou have visited:"
prompt += "\n(Enter 'quit' when you are finished.) \n"

# A loop that starts with while True 1 will run forever unless it reaches a break statement.
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"\nI'd love to go to {city.title()}!")