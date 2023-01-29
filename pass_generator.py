
import random
import string

print("Welcome to the Random Password Generator!")

words = input("Please enter 3 words to generate your password (separated by spaces): ").split()

# Generate random numbers
rand1 = str(random.randint(0, 9))
rand2 = str(random.randint(0, 9))
rand3 = str(random.randint(0, 9))

# Generate random symbols
symb1 = random.choice(string.punctuation)
symb2 = random.choice(string.punctuation)

# Generate random letters
char1 = random.choice(string.ascii_lowercase)
char2 = random.choice(string.ascii_lowercase)

# Generate the password
password = words[0][:2] + rand1 + symb1 + words[1][:2] + rand2 + symb2 + words[2][:2] + rand3 + char1 + char2

print("Your new password is: " + password)
