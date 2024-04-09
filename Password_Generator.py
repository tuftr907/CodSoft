import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            # Get desired pass length 
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue

            password = generate_password(length)
            print("Generated Password:", password)

            response = input("Do you want to generate another password? (yes/no): ").lower()
            if response != 'yes':
                print("Thank you for using the Password Generator.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
