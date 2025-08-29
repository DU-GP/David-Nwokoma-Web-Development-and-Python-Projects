

# ------------------ Guessing Game ----------------------

Secret_number = 9
Guess_count = 0
Guess_limit = 3 

while Guess_count < Guess_limit:
    Guess = int(input("Guess: "))
    Guess_count += 1
    if Guess == Secret_number:
        print (" You Won!")
        break
else:
    print(" Try again! ")


secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
else:
    print("Try again!")
