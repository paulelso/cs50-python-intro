# Vanity Plates

Vanity Plates is a Python Loops problem challenge. As per <https://cs50.harvard.edu/python/2022/psets/2/plates/>

The requirements are:
- All vanity plates must start with at least two letters.”
- Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- Numbers cannot be used in the middle of a plate; they must come at the end. E.g., AAA222 is acceptable; AAA22A would not be acceptable. 
- The first number used cannot be a ‘0’.”
- No periods, spaces, or punctuation marks are allowed.

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).