"""Mutating functions."""

__author__ = "730669462"

my_list: list[int] = [1, 2, 3]


def manual_append(name_a: list[int], name_b: int) -> None: 
    """Manual append."""
    name_a.append(name_b)


def double(name_a: list[int]) -> None:
    """Double fnc."""
    tracker_a: int = 0
    
    while tracker_a < len(name_a):
        score: int = name_a[tracker_a] * 2
        name_a[tracker_a] = score
        tracker_a += 1