import logging
from getpass import getpass  # For hidden password input

from constructormy import Afsal

# Configure logging
logging.basicConfig(filename="login_attempts.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class LoginPage:
    MAX_ATTEMPTS = 3  # Limit login attempts

    def __init__(self):
        self.username = "admin"
        self.password = "password123"

    def authenticate(self, username, password):
        """Simulated authentication function. Replace with database validation."""
        return username == "admin" and password == "password123"

    def login(self):
        attempts = 0
        while attempts < self.MAX_ATTEMPTS:
            try:
                self.username = input("Enter username: ")
                self.password = input(
                    "Enter password: ")  # Replace getpass with input for testing  # Secure password input

                if not self.username or not self.password:
                    raise ValueError("Username and password cannot be empty")

                if self.authenticate(self.username, self.password):
                    print("Login successful!")
                    logging.info(f"Successful login attempt by {self.username}")
                    return  # Exit on successful login
                else:
                    attempts += 1
                    logging.warning(f"Failed login attempt {attempts} for user {self.username}")
                    print(f"Invalid credentials. Attempts remaining: {self.MAX_ATTEMPTS - attempts}")

            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                print(f"An unexpected error occurred. Please try again.")

        print("Too many failed attempts. Try again later.")


# Usage
if __name__ == "__main__":
    login_page = LoginPage()
    login_page.login()
