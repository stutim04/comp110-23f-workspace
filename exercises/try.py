"""Functional Battleship."""
__author__ = "730669462"

import random


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size = 4
secret_row = 3
secret_column = 2


def input_guess(grid_size: int, specification: str) -> int:
    assert specification == "row" or specification == "column"
    guess = int(input(f"Guess a {specification}: "))
    if guess < 1 or guess > grid_size:
        while True:
            guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            if guess >= 1 and guess <= grid_size:
                break
            else:
                continue
    return guess

def print_grid(grid_size: int, row_guess: int, column_guess: int, user_guess: bool) -> None:
    # Determine the width needed for printing column numbers
    col_width = len(str(grid_size))
    # Print column numbers
    print("    ", end="")
    for col in range(1, grid_size + 1):
        print(f"{col:>{col_width}}", end="")
    print()  # Newline after printing column numbers
    
    for row in range(1, grid_size + 1):
        # Print row numbers
        print(f"{row:>{col_width}} ", end="")
        # Print emoji boxes
        for col in range(1, grid_size + 1):
            if row == row_guess and col == column_guess and user_guess:
                print(RED_BOX, end="")
            elif row == secret_row and col == secret_column:
                print(BLUE_BOX, end="")
            else:
                print(WHITE_BOX, end="")
        print()  # Newline after printing each row

def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    return secret_row == row_guess and secret_column == column_guess

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    num_turns = 5
    turn = 1
    user_won = False

    while turn <= num_turns and not user_won:
        print(f"=== Turn {turn}/{num_turns} ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        user_won = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, user_won)
        if user_won:
            print(f"Hit!\nYou won in {turn}/{num_turns} turns!")
        else:
            print("Miss!")
        turn += 1
        if not user_won: 
            print(f"X/{num_turns} - Better luck next time!")

if __name__ == "__main__":
        grid_size: int = random.randint(3, 5)
        main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
