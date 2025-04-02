text1 = "   "
print(text1.isspace())  # Output: True (only spaces)

text2 = "\t\n  "
print(text2.isspace())  # Output: True (contains tabs and newlines)

text3 = "Hello world"
print(text3.isspace())  # Output: False (contains non-whitespace characters)

text4 = ""
print(text4.isspace())  # Output: False (empty string)
