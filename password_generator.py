import random

# Lists of characters for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# List to store the generated password
password_list = []

print("Welcome to the PyPassword Generator!")

# User input for password preferences
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Generate password based on user preferences
for _ in range(num_letters):
    password_list.append(random.choice(letters))

for _ in range(num_symbols):
    password_list.append(random.choice(symbols))

for _ in range(num_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password characters
random.shuffle(password_list)

# Convert the list to a string to create the final password
generated_password = ''.join(password_list)

# Print the generated password
print("Your generated password is:", generated_password)
