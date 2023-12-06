# Prompt the user for a variable name in camel case
camel_case = input("camelCase: ")

# Convert camel case to snake case
snake_case = ''.join(['_' + c.lower() if c.isupper() else c for c in camel_case]).lstrip('_')

# Output the corresponding name in snake case
print("snake_case:", snake_case)