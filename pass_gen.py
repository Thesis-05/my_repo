import random

print("\nWelcome to password Generator")

characters = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*")

Amount_of_passwords = input("\nEnter the amount of password here: ")
Amount_of_passwords = int(Amount_of_passwords)

Number_of_characters_in_the_password = input("\nEnter the number of characters of password you want: ")
Number_of_characters_in_the_password = int(Number_of_characters_in_the_password)

print("\n Here is your password: ")


for password in range(Amount_of_passwords):
    password = " "
    for c in range(Number_of_characters_in_the_password):
        password += random.choice(characters)

    print(password)


