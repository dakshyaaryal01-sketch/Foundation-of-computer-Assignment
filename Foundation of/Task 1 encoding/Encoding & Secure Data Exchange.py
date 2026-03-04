import base64

message = "Hello Secure World"

encoded = base64.b64encode(message.encode())
decoded = base64.b64decode(encoded)

print("Original:", message)
print("Encoded:", encoded)
print("Decoded:", decoded.decode())