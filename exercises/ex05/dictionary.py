"""Dictionary Utility Functions."""


__author__ = "730669462"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert."""
    inverted_dict: dict[str, str] = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Error in invert!")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Favorite Color."""
    color_count: dict[str, int] = {}
    for key in input_dict.values():
        if key not in color_count:
            color_count[key] = 1
        else:
            color_count[key] += 1
    most_popular_color = max(color_count, key=lambda x: color_count[x])
    return most_popular_color


def count(input_list: list[str]) -> dict[str, int]:
    """Count."""
    counts: dict[str, int] = {}
    for key in input_list:
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    return counts


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Alphabetizer."""
    alphabet_dict: dict[str, list[str]] = {}
    for key in input_list:
        first_letter = key[0].lower()
        if first_letter in alphabet_dict:
            alphabet_dict[first_letter].append(key)
        else:
            alphabet_dict[first_letter] = [key]
    return alphabet_dict


def update_attendance(input_dict: dict[str, list[str]], day: str, name: str) -> None:
    """Updated attendance."""
    if day in input_dict:
        input_dict[day].append(name)
    else:
        input_dict[day] = [name]