from random import randint
num = randint(1, 100)
a = -1
guesses = 0

while (a!=num):
    a = int(input("Guess the number:"))
    if a==num:
        print(f"You guessed the number! The number was {num}")
        print(f"You guessed the number in {guesses} attempt(s).")
    elif a>num:
        print("Lower number please!")
        guesses+=1
    elif a<num:
        print("Higher number please!")
        guesses += 1
    else:
        print("Invalid input.")