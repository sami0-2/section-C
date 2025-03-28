text = "Hello, world! Hello again!"
print(text.replace("Hello", "Hi"))  # Output: "Hi, world! Hi again!"
print(text.replace("o", "O"))       # Output: "HellO, wOrld! HellO again!"
print(text.replace("Hello", "Hi", 1))  # Output: "Hi, world! Hello again!" (only replaces the first occurrence)
print(text.replace("Python", "Java"))  # Output: "Hello, world! Hello again!" (no change since "Python" isn't in the string)