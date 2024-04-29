import random

print("Welcome to the Guess the number game\n")

print("Number is between 1-5\n")

guess_count = 0
guess_limit = 3
secret_number = random.randint(1, 5)

while guess_count < guess_limit:
    your_guess = int(input("your Guess: "))
    guess_count += 1
    
    if your_guess == secret_number:
        print("you won!!")
        break

    elif your_guess < secret_number:
        print("higher")
    
    elif your_guess > secret_number:
        print("lower")

    else:
        print("wrong guess")

print("\nThe correct number was: " + str(secret_number) + "\n")
