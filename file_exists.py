# Import the 'os' module, which provides a way to interact with the operating system.
import os

# Set the variable 'path' to the string 'While-loop.py', representing a file path.
# Define the file path as a string
path = 'While-loop.py'

# Use the 'os.path.exists()' function to check if the file specified by 'path' exists.
# It returns True if the file exists, and False if it doesn't.
print(os.path.exists(path))

