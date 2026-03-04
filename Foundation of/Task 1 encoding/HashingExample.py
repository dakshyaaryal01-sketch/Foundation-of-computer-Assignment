import hashlib

password = "mypassword"
hash_value = hashlib.sha256(password.encode()).hexdigest()

print("SHA-256 Hash:", hash_value)