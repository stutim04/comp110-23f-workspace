"""Functional Battleship."""
__author__ = "730669462"

import random


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

secret_row = 3
secret_column = 2


def input_guess(grid_size: int, specification: str) -> int:
    """Take user input for row or column guess."""
    assert specification == "row" or specification == "column"
    guess: int = int(input(f"Guess a {specification}: "))
    if guess < 1 or guess > grid_size:
        while True:
            guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            if guess >= 1 and guess <= grid_size:
                break
            else:
                continue
    return guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, user_guess: bool) -> None:
    """Print the grid with user's guess."""
    result_box: str = ""
    if user_guess:
        result_box = RED_BOX
    else:
        result_box = WHITE_BOX

    row_counter: int = 1
    while row_counter <= grid_size:
        emoji_boxes: str = ""
        column_counter: int = 1
        if row_counter == row_guess:
            while column_counter <= grid_size:
                if column_counter == column_guess:
                    emoji_boxes += result_box
                    column_counter += 1
                else: 
                    emoji_boxes += BLUE_BOX
                    column_counter += 1
        else:
            while column_counter <= grid_size:
                emoji_boxes += BLUE_BOX
                column_counter += 1
        print(emoji_boxes)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Print the grid with user's guess."""   
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main function to run the game."""
    turn: int = 1
    while turn <= 5: 
        print(f"=== Turn {turn}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        user_won: bool = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, user_won)
        if user_won:
            print(f"Hit! You won in {turn}/5 turns!")
            return
        else:
            print("Miss!")
        turn += 1
    print(f"{turn}/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))