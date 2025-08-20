# 11.03 Employee

class Employee:
    """Collect employee data."""

    def __init__(self, first_name, last_name, annual_salary):
        """Store employee information."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Give employee a raise."""
        print(f"{self.first_name} {self.last_name}'s salary is currently {self.annual_salary}.")
        self.annual_salary += raise_amount
        print(f"{self.first_name}'s salary is now {self.annual_salary}.")
        