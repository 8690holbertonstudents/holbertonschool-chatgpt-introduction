#!/usr/bin/python3
# Shebang line for Python 3

import sys  # Importing sys to use command-line arguments

# Function to calculate the factorial of a non-negative integer recursively
# Parameters:
# - n (int): The number for which the factorial
# is to be calculated. Should be a non-negative integer.
# Returns:
#   - int: The factorial of the given number 'n'


def factorial(n):
    # If n is 0, return 1 as 0! = 1
    if n == 0:
        return 1
    else:
        # Otherwise, calculate factorial recursively
        # by calling itself with (n - 1)
        return n * factorial(n - 1)

# Fetch the first command-line argument and convert it to an integer
# This argument represents the number whose factorial is to be calculated


n = int(sys.argv[1])

# Calculate the factorial of the provided number
f = factorial(n)

# Print the result to the console
print(f)
