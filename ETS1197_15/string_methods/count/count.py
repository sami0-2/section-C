text = "Hello, world! Hello again!"
print(text.count("Hello"))  # Output: 2
print(text.count("o"))      # Output: 3
print(text.count("l", 0, 5))  # Output: 2 (counts only in "Hello")
print(text.count("Python")) # Output: 0 (not found)