#!/usr/bin/python3
# Shebang line for Python 3

# Importing required modules
import sys  # To exit the script gracefully

# Checkbook class simulates a simple bank account with deposit,
# withdrawal, and balance-checking features.


class Checkbook:
    def __init__(self):
        # Initialize the balance to zero
        self.balance = 0.0

    # Deposit money into the checkbook.
    # Parameters:
    #   - amount (float): The amount to be deposited.
    # Returns:
    #   - None (prints the new balance after deposit)
    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    # Withdraw money from the checkbook.
    # Parameters:
    #   - amount (float): The amount to withdraw.
    # Returns:
    #   - None (prints the new balance after
    # withdrawal or an insufficient funds message)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    # Get the current balance in the checkbook.
    # Parameters:
    #   - None
    # Returns:
    #   - None (prints the current balance)
    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

# Main function to interact with the Checkbook.
# Allows user to deposit, withdraw, check balance, or exit.


def main():
    # Create an instance of Checkbook
    cb = Checkbook()

    # Loop for user interaction
    while True:
        action = input("What would you like to do? \
                (deposit, withdraw, balance, exit): ").lower()

        # Exit condition
        if action == 'exit':
            break

        # Handle deposit with error checking for valid numeric input
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        # Handle withdrawal with error checking for valid numeric input
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    raise ValueError("Withdrawal amount must be positive.")
                cb.withdraw(amount)
            except ValueError as ve:
                print(f"Error: {ve}. Please enter a valid positive amount.")

        # Get the current balance
        elif action == 'balance':
            cb.get_balance()

        # Invalid action
        else:
            print("Invalid command. Please try again.")

# Run the main function


if __name__ == "__main__":
    main()
