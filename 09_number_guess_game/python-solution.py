import random

number = random.randint(1, 100)

print("Guess a number between 1 and 100")

while True:
    guess = int(input("Your guess: "))

    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too High")
    else:
        print("Correct! You guessed the number.")
        break
