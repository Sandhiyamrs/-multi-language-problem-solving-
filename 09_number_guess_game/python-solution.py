import random
num = random.randint(1,100)
attempts=0
while True:
    guess = int(input("Guess number (1-100): "))
    attempts+=1
    if guess<num: print("Higher!")
    elif guess>num: print("Lower!")
    else: break
print(f"Correct! Attempts: {attempts}")
