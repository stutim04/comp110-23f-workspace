"""List Utility Functions."""

__author__ = "730669462"


def all(lst: list[int], num: int) -> bool:
    """Defining All."""
    if not lst:
        return False
    for item in lst:
        if item != num:
            return False
    return True


def max(lst: list[int]) -> int:
    """Defining Max."""
    if not lst:
        raise ValueError("max() arg is an empty List")
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Defining Is Equal."""
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


def extend(lst1: list[int], lst2: list[int]) -> None:
    """Defining Extended."""
    lst1.extend(lst2)