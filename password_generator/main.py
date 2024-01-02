# Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

try:
    # Get user input for the number of characters
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Generate random samples for letters, numbers, and symbols
    ran_letters = (random.choices(letters, k=nr_letters))
    ran_numbers = (random.choices(numbers, k=nr_numbers))
    ran_symbols = (random.choices(symbols, k=nr_symbols))

    # Combine the lists into a single list
    password_list = ran_letters + ran_numbers + ran_symbols

    # Shuffle the combined list to randomize the order
    random.shuffle(password_list)

    # Convert the list to a string and print the password
    password = "".join(password_list)
    print(password)

except ValueError:
    print("Please enter a valid number.")
