class User:
    """A simple attempt to try and model a user."""
    def __init__(self, first_name, last_name, class_type, country_of_origin):
        """Initializing user and user data"""
        self.first_name = first_name
        self.last_name = last_name
        self.class_type = class_type
        self.country_of_origin = country_of_origin
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Class Type: {self.class_type.title()}")
        print(f"Place of Origin: {self.country_of_origin.title()}")

    def greet_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} the {self.class_type.title()}, welcome.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0