"""Dictionary Test."""

__author__ = "730669462"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance 
import pytest


def test_invert_empty() -> None:
    """Test invert empty."""
    assert invert({}) == {}


def test_invert() -> None:
    """Test invert input."""
    test = {'strawberry': 'kiwi', 'yellow': 'banana', 'beans': 'lettuce'}
    assert invert(test) == {'kiwi': 'strawberry', 'banana': 'yellow', 'lettuce': 'beans'}


def test_invert_one() -> None:
    """Test invert with repeating values."""
    my_dictionary = {'a': 'b', 'y': 'x'}
    with pytest.raises(KeyError):
        invert(my_dictionary)


def test_favorite_color_empty() -> None:
    """Test favorite color empty."""
    assert favorite_color({}) == ""


def test_favorite_color() -> None:
    """Test favorite color with colors."""
    test = {'sara': 'yellow', 'caroline': 'purple', 'stuti': 'blue'}
    assert favorite_color(test) == 'blue'


def test_other_colors() -> None:
    """Testing other colors."""
    test = {'sophia': 'teal', 'cole': 'green', 'aarav': 'orange'}
    assert favorite_color(test) == 'teal'


def test_count_empty() -> None:
    """Test count with empty list."""
    assert count([]) == {}


def test_count() -> None:
    """Test count with a list."""
    test_list = ['pink', 'purple']
    assert count(test_list) == {'pink': 1, 'purple': 1}


def test_count_one() -> None:
    """Test count function elems."""
    assert count(['pink', 'purple', 'red', 'pink', 'purple']) == {'pink': 2, 'purple': 2, 'red': 1}


def test_alphabetizer_empty() -> None:
    """Test alphabetizer empty."""
    assert alphabetizer([]) == {}


def test_alphabetizer() -> None:
    """Test alphabetizer with list."""
    list_one = ['stuti', 'sara', 'caroline']
    expected_result = {'s': ['stuti', 'sara'], 'c': ['caroline']}
    assert alphabetizer(list_one) == expected_result


def test_alphabetizer_one() -> None:
    """Test alphabetizer with same words."""
    list_one = ['stuti', 'sara', 'caroline', 'cole', 'sophia']
    expected_result = {'s': ['stuti', 'sara', 'sophia'], 'c': ['caroline', 'cole']}
    assert alphabetizer(list_one) == expected_result


def test_update_attendance_empty() -> None:
    """Test update attendance empty."""
    assert update_attendance({}, 'Saturday', 'Sara') == {'Saturday': ['Sara']}


def test_update_attendance() -> None:
    """Test update attendance with attendance."""
    test_update = {'Saturday': ['Stuti', 'Sara'], 'Sunday': ['Sophia']}
    assert update_attendance(test_update, 'Saturday', 'Cole') == {'Saturday': ['Stuti', 'Sara', 'Cole'], 'Sunday': ['Sophia']}


def test_update_attendance_one() -> None:
    """Test update attendance with same attendance."""
    test_update = {'Saturday': ['Stuti', 'Sara'], 'Sunday': ['Sophia']}
    assert update_attendance(test_update, 'Sunday', 'Sujan') == {'Saturday': ['Stuti', 'Sara'], 'Sunday': ['Sophia', 'Sujan']}