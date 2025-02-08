# The \w character class is equivalent to [a-zA-Z0-9_]
# Therefore, the \W character class is equivalent to [^a-zA-Z0-9_]
# A character class is created by square brackets: 
# [a-z] -> class of all the characters from a to z in lowercase

import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        
        # '\d' -> means all digits
        # r' ' -> means a raw string
        
        constraints = [
            (nums, r'\d'), 
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
    
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
