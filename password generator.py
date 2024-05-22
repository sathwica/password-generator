import string
import random

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_characters=True):
    # Base character set
    characters = list(string.ascii_lowercase)
    
    # Add additional character sets based on user preferences
    if include_uppercase:
        characters.extend(string.ascii_uppercase)
    if include_numbers:
        characters.extend(string.digits)
    if include_special_characters:
        characters.extend(string.punctuation)
    
    # Ensure there's at least one character from each chosen set
    password = []
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_numbers:
        password.append(random.choice(string.digits))
    if include_special_characters:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password length
    while len(password) < length:
        password.append(random.choice(characters))
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    # Join the list to form the final password string
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    print("----------------------------------")
    
    # Get user input for the number of passwords
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Generate passwords
    passwords = []
    for i in range(num_passwords):
        while True:
            try:
                password_length = int(input(f"Enter the length of password {i + 1} (minimum 3): "))
                if password_length < 3:
                    print("Password length should be at least 3. Setting to 3.")
                    password_length = 3
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Generate and store the password
        generated_password = generate_password(length=password_length)
        passwords.append(generated_password)
    
    # Display generated passwords
    print("\nGenerated Passwords:")
    print("--------------------")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")
    
    # Wait for user to press Enter before exiting
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
