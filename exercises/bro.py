"""Dictionary Test."""

__author__ = "730669462"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_empty_edge() -> None:
    """Test invert empty."""
    assert invert({}) == {}


def test_invert_use() -> None:
    """Test invert input."""
    test: dict[str, str] = {'strawberry': 'kiwi', 'yellow': 'banana', 'beans': 'lettuce'}
    assert invert(test) == {'kiwi': 'strawberry', 'banana': 'yellow', 'lettuce': 'beans'}


def test_invert_one_use() -> None:
    """Test invert with repeating values."""
    with pytest.raises(KeyError):
        my_dictionary = {'a': 'c', 'd': 'c'}
        invert(my_dictionary)


def test_favorite_color_empty_edge() -> None:
    """Test favorite color empty."""
    test_empty: dict[str, str] = {}
    assert favorite_color(test_empty) == ""


def test_favorite_color_use() -> None:
    """Test favorite color with colors."""
    test: dict[str, str] = {'sara': 'yellow', 'caroline': 'purple', 'stuti': 'blue'}
    assert favorite_color(test) == 'blue'


def test_other_colors_use() -> None:
    """Testing other colors."""
    test: dict[str, str] = {'sophia': 'teal', 'cole': 'green', 'aarav': 'orange'}
    assert favorite_color(test) == 'teal'


def test_count_empty_edge() -> None:
    """Test count with empty list."""
    test: list[str] = []
    assert count(test) == {}


def test_count_use() -> None:
    """Test count with a list."""
    test_list: list[str] = ['pink', 'purple']
    assert count(test_list) == {'pink': 1, 'purple': 1}


def test_count_one_use() -> None:
    """Test count function elems."""
    assert count(['pink', 'purple', 'red', 'pink', 'purple']) == {'pink': 2, 'purple': 2, 'red': 1}


def test_alphabetizer_empty_edge() -> None:
    """Test alphabetizer empty."""
    list_one: list[str] = []
    assert alphabetizer(list_one) == {}


def test_alphabetizer_use() -> None:
    """Test alphabetizer with list."""
    list_one: list[str] = ['stuti', 'sara', 'caroline']
    expected_result = {'s': ['stuti', 'sara'], 'c': ['caroline']}
    assert alphabetizer(list_one) == expected_result


def test_alphabetizer_one_use() -> None:
    """Test alphabetizer with same words."""
    list_one: list[str] = ['stuti', 'sara', 'caroline', 'cole', 'sophia']
    expected_result = {'s': ['stuti', 'sara', 'sophia'], 'c': ['caroline', 'cole']}
    assert alphabetizer(list_one) == expected_result


def test_update_attendance_empty_edge() -> None:
    """Test update attendance empty."""
    test_update: dict[str, list[str]] = {}
    assert update_attendance(test_update, 'Saturday', 'Sara') == {'Saturday': ['Sara']}


def test_update_attendance_use() -> None:
    """Test update attendance with attendance."""
    test_update: dict[str, list[str]] = {'Saturday': ['Stuti', 'Sara'], 'Sunday': ['Sophia']}
    assert update_attendance(test_update, 'Saturday', 'Cole') == {'Saturday': ['Stuti', 'Sara', 'Cole'], 'Sunday': ['Sophia']}


def test_update_attendance_one_use() -> None:
    """Test update attendance with same attendance."""
    test_update: dict[str, list[str]] = {'Saturday': ['Stuti', 'Sara'], 'Sunday': ['Sophia']}
    assert update_attendance(test_update, 'Sunday', 'Sujan') == {'Saturday': ['Stuti', 'Sara'], 'Sunday': ['Sophia', 'Sujan']}
