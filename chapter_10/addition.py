# 10.6 Addition

def addition():
    a = input("Please enter the first number: \n")
    b = input("Please enter the second number: \n")
    try:
        print(f"Your total is: {int(a) + int(b)}")
    except ValueError:
        print("\nPlease enter a valid number.")

# addition()

