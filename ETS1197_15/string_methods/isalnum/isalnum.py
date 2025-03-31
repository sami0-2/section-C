text1 = "Hello123"
print(text1.isalnum())  # Output: True (contains only letters and digits)

text2 = "Hello 123"
print(text2.isalnum())  # Output: False (contains a space)

text3 = "Hello!"
print(text3.isalnum())  # Output: False (contains punctuation)

text4 = "12345"
print(text4.isalnum())  # Output: True (contains only digits)

text5 = ""
print(text5.isalnum())  # Output: False (empty string)