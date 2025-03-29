text = "  Hello, world!  "
print(text.rstrip())        # Output: "  Hello, world!" (removes trailing spaces)

text2 = "---Hello---"
print(text2.rstrip("-"))    # Output: "---Hello" (removes trailing '-')

text3 = "xyzHelloxyz"
print(text3.rstrip("xyz"))  # Output: "xyzHello" (removes 'x', 'y', and 'z' from the end)

text4 = "  Hello  "
print(text4.rstrip(" "))    # Output: "  Hello" (explicitly removes spaces from the end)
