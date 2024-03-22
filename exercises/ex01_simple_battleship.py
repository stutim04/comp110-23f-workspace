"""EX01 - Simple Battleship - A cute step towards Battleship."""

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

secret_boat_location = int(input("Pick a secret boat location between 1 and 4: "))
if secret_boat_location < 1:
    print("Error! " + str(secret_boat_location) + " too low!")
    exit()
if secret_boat_location > 4:
    print("Error! " + str(secret_boat_location) + " too high!")
    exit()

secret_boat_guess = int(input("Guess a number between 1 and 4: "))
if secret_boat_guess < 1:
    print("Error! " + str(secret_boat_guess) + " too low!")
    exit()
if secret_boat_guess > 4:
    print("Error! " + str(secret_boat_guess) + " too high!")
    exit()

if secret_boat_location == secret_boat_guess:
    if secret_boat_guess == 1:
        print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if secret_boat_guess == 2:
        print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
    if secret_boat_guess == 3:
        print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
    if secret_boat_guess == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
    print("Correct! You hit the ship. ")
else:
    if secret_boat_guess == 1:
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if secret_boat_guess == 2:
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
    if secret_boat_guess == 3:
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
    if secret_boat_guess == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
    print("Incorrect! You missed the ship. ")

__author__ = "730669462"