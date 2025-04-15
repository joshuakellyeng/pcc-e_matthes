# How the input() Function Works

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# Letting the User Choose When to Quit

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. \n"

# message = ''
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

# Using a Flag

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. \n"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)