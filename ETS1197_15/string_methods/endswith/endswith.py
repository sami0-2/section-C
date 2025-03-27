text = "Hello, world!"
print(text.endswith("world!"))  # Output: True
print(text.endswith("Hello"))   # Output: False
print(text.endswith("world", 0, 12))  # Output: True (checks up to index 12)
print(text.endswith("o", 0, 5))  # Output: True (checks only first 5 characters)