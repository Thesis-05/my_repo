print("""\n============================================welcome to the guess the number game========================================================""")

guess_count = 0
guess_limit = 3
secret_number = 5
print("\nThe number is between 1-5")
while guess_count < guess_limit:
    guess = int(input("your Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Yeah, you won!")
        break
    else:
        print("wrong! guess")
