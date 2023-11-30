# Prompts the user for an arithmetic expression.
expression = input("Expression: ")

# Splits the expression into three parts: x, operator, and z.
x, operator, z = expression.split()

# Converts x and z to integers.
x = int(x)
z = int(z)

# Performs the arithmetic operation based on the operator.
if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    result = x / z

# Outputs the result as a floating-point value formatted to 1 decimal place.
print(f"{result:.1f}")