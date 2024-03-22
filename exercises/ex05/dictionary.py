"""Dictionary Utility Functions."""


__author__ = "730669462"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Dictionary of invert."""
    input_2: dict[str, str] = {}
    for keys in input:
        if input[keys] in input_2: 
            raise KeyError("error in invert!")
        else:
            input_2[input[keys]] = keys
    return input_2


def favorite_color(input: dict[str, str]) -> str:
    """Favorite Colors."""
    d: dict[str, int] = {}
    for key in input:
        if input[key] not in d:
            d[input[key]] = 1
        else:
            d[input[key]] += 1
    color: str = ""
    number: int = 0
    for key in d:
        if d[key] > number:
            color = key
        number = d[key]
    return color


def count(input: list[str]) -> dict[str, int]:
    """Count."""
    input_2: dict[str, int] = {}
    for keys in input:
        if keys in input_2: 
            input_2[keys] += 1
        else: 
            input_2[keys] = 1
    return input_2 


def alphabetizer(inputs: list[str]) -> dict[str, list[str]]: 
    """Alphabetizer."""
    input_1: dict[str, list[str]] = {}
    for key in inputs:
        letter: str = key[0].lower()
        if letter in input_1:
            input_1[letter].append(key)
        else:
            input_1[letter] = [key]
    return input_1


def update_attendance(input_1: dict[str, list[str]], day: str, name: str) -> None:
    """Update Attendance."""
    if day in input_1: 
        input_1[day].append(name)
    else:
        input_1[day] = [name]
    return None
