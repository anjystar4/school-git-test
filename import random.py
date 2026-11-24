import random

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""

    for _ in range(12):
        password += random.choice(characters)

    return password


print("School Git Test")
print("Generated password:", generate_password())