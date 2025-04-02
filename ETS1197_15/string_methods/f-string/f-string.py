# Basic usage
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Output: "My name is Alice and I am 25 years old."

# Inline calculations
x, y = 5, 10
print(f"The sum of {x} and {y} is {x + y}.")
# Output: "The sum of 5 and 10 is 15."

# Formatting numbers
pi = 3.14159
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
# Output: "Pi rounded to 2 decimal places: 3.14"

# Using functions inside f-strings
def greet(name):
    return f"Hello, {name}!"

print(f"{greet('Bob')}, welcome!")
# Output: "Hello, Bob!, welcome!"
