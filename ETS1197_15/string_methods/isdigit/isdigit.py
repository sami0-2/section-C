text1 = "12345"
print(text1.isdigit())  # Output: True (all characters are digits)

text2 = "123abc"
print(text2.isdigit())  # Output: False (contains letters)

text3 = "123.45"
print(text3.isdigit())  # Output: False (contains a decimal point)

text4 = "²³"
print(text4.isdigit())  # Output: True (Unicode superscript digits)

text5 = ""
print(text5.isdigit())  # Output: False (empty string)
