# Basic usage
text = "Hello"
encoded = text.encode()
print(encoded)  # Output: b'Hello'

# Encoding with non-ASCII characters
text = "café"
print(text.encode())        # Output: b'caf\xc3\xa9'
print(text.encode('ascii', 'ignore'))  # Output: b'caf'

# Using 'replace' to handle errors
print(text.encode('ascii', 'replace'))  # Output: b'caf?'
