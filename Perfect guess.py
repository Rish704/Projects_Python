import random
ran = random.randint(1, 100)
a = None
guesses = 0

while a != ran:
    a = int(input("Guess the number: "))
    guesses += 1
    if a == ran:
        print(f"you guessed the number right in {guesses} attempt")
    elif a > ran:
        print("The number is lower than that! Try again")
    elif a < ran:
        print("The number is higher than that! Try again")
with open("highscore.txt", "r") as f:
    read = int(f.read())
if guesses < read:
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))
    print(f"The new highscore is {guesses}")
else:
    print(f"The highscore is {read}")