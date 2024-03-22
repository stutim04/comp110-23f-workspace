"""Praciting."""

def odd_and_even(name_1: list[int]) -> list[int]:
    new_list: list[int] = []
    ind_tracker: int = 0
    for elem in name_1:
        if elem % 2 == 1 and ind_tracker % 2 == 0:
            new_list.append(elem)
        ind_tracker += 1
    return new_list

def short_word(name_2: list[str]) -> list[str]:
    new_list_2: list[str] = []
    for elem in name_2:
        if len(elem) < 5:
            new_list_2.append(elem)
        else:
            print(f"{elem} was too long.")
    return new_list_2

list1: list[str] = ["poop", "fart", "shithead"]
print(short_word(list1))