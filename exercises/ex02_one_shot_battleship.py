"""EX02 - One Shot Battleship."""

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size = 4
secret_row = 3
secret_column = 2

result = ""
hit_target = False

guess_row = int(input("Guess a row: "))
if guess_row < 1 or guess_row > grid_size:
    while True:
        guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        if guess_row >= 1 and guess_row <= grid_size:
            break
        else:
            continue
guess_column = int(input("Guess a column: "))
if guess_column < 1 or guess_column > grid_size:
    while True:
        guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        if guess_column >= 1 and guess_column <= grid_size:
            break
        else:
            continue
if guess_row == secret_row and guess_column == secret_column:
    hit_target = True
    result = RED_BOX
else:
    result = WHITE_BOX

for row_counter in range(1, grid_size + 1):
    emoji_boxes = ""
    for column_counter in range(1, grid_size + 1):
        if row_counter == guess_row and column_counter == guess_column:
            emoji_boxes += result
        else:
            emoji_boxes += BLUE_BOX
    print(emoji_boxes)

if hit_target:
    print("Hit!")
else:
    if guess_row < 1 or guess_row > grid_size or guess_column < 1 or guess_column > grid_size:
        print("Miss!")
    else:
        if guess_row == secret_row:
            print("Close! Correct row, wrong column.")
        elif guess_column == secret_column:
            print("Close! Correct column, wrong row.")
        else:
            print("Miss!")

__author__ = "730669462"