# Basic formatting
text = "Hello, {}!"
print(text.format("Alice"))  # Output: "Hello, Alice!"

# Formatting multiple values
text = "My name is {} and I am {} years old."
print(text.format("Bob", 25))  # Output: "My name is Bob and I am 25 years old."

# Using positional arguments
text = "I love {1} more than {0}."
print(text.format("Java", "Python"))  # Output: "I love Python more than Java."

# Using named placeholders
text = "I am {name} and I study {subject}."
print(text.format(name="Alice", subject="Engineering"))  
# Output: "I am Alice and I study Engineering."

# Formatting numbers
num = 3.14159
print("Pi is approximately {:.2f}".format(num))  # Output: "Pi is approximately 3.14"
