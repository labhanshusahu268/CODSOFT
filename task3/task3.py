import random
import string

def generate_password():
    length = int(input("enter the length of password : "))
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print(" Welcome to the Password Generator ")
    
    try:
        password = generate_password()
        print(f"\n Generated Password: {password}")
    except ValueError:
        print(" Invalid input. Please enter a number.")

# Run the program
main()
