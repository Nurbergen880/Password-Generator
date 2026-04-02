import random
import string

def generate_password(length):
    if length < 4:
        return "Password must be at least 4 characters long"

    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)

    # максимум 2 спец символа
    num_special = random.randint(0, 2)
    special_chars = [random.choice(string.punctuation) for _ in range(num_special)]

    remaining_length = length - (3 + num_special)

    other_chars = string.ascii_letters + string.digits
    rest = [random.choice(other_chars) for _ in range(remaining_length)]

    password_list = [uppercase, lowercase, digit] + special_chars + rest

    random.shuffle(password_list)

    return ''.join(password_list)


length = int(input("Enter password length: "))
password = generate_password(length)

print("Generated password:", password)