text1 = "Hello"
print(text1.isalpha())  # Output: True (all letters)

text2 = "Hello123"
print(text2.isalpha())  # Output: False (contains numbers)

text3 = "Hello!"
print(text3.isalpha())  # Output: False (contains punctuation)

text4 = " "
print(text4.isalpha())  # Output: False (contains only whitespace)

text5 = ""
print(text5.isalpha())  # Output: False (empty string)