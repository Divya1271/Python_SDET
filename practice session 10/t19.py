import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random characters from all sets
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return it
    return ''.join(password)

# Example usage:
password_length = 12
print("Generated password:", generate_password(password_length))
