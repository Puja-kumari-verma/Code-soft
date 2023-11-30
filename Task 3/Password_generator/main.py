import random
import string

def generate_password(length):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine character sets based on complexity
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Ensure the password length is at least 4 characters
    length = max(length, 4)

    # Generate password
    password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits) + random.choice(symbols)
    password += ''.join(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle password characters for randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def main():
    # Get user input for password length
    try:
        password_length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Generate and display the password
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

if _name_ == "_main_":
    main()

