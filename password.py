import random
import string
import time
def generate_password(length = 12, include_digits = True, include_special_chars = True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    password = " ".join(random.choice(characters)for _ in range(length)) #Password
    return password
def print_password_strength(password):
    strength = len(set(password))/len(password)
    strength_percentage = int(strength * 100)
    print(f"\n Strength Percentage: {strength_percentage}%")
    print("Password Strength: ")
    print("["+"="*strength_percentage+">"+" "*(100-strength_percentage)+"]") #Formula
if __name__ == '__main__':
    password_length = int(input("Enter the desired length of the password: "))
    include_digits = input("Include digits? (y/n): ").lower()=='y'           #Include Syntax
    include_special_chars = input("Include Special Characters? (y/n): ").lower()=='y' # Include Syntax
    print(f"\n Generated Password: {generate_password}")
    time.sleep(1)
    print("Generated Password: ... \n")
    generated_password = generate_password(password_length, include_digits, include_special_chars)
    print(f"\n Generated Password: {generated_password}")
    print_password_strength(generated_password)
