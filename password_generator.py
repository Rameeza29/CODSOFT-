import random  # Import the random module to generate random characters

y = int(input("Enter length num: "))  
# Take user input for the desired password length and convert it to integer

r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-={}[]|\":;'<>?,./~`"  
# String containing uppercase letters, lowercase letters, digits, and special characters

lst = []  
# Create an empty list to store randomly selected characters

for i in range(y):  
    # Loop runs 'y' times (password length)
    lst.append(random.choice(r))  
    # Select a random character from string 'r' and add it to the list

print("Password:", "".join(lst))  
# Join all characters in the list into a single string and print the password