# Writing Clear Prompts
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")


# How to build prompts over several lines
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
