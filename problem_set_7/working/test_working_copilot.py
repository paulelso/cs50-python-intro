import pytest
from working import convert, convert_to_24_hour


def main():
    test_convert_valid_input()
    test_convert_invalid_input()
    test_convert_to_24_hour()


def test_convert_valid_input():
    assert convert("10:30 AM to 2:45 PM") == "10:30 to 14:45"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"


def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("10:30 AM to 2:45")
    with pytest.raises(ValueError):
        convert("9 AM to 5 PM to 6 PM")


def test_convert_to_24_hour():
    assert convert_to_24_hour("10:30 AM") == "10:30"
    assert convert_to_24_hour("2:45 PM") == "14:45"
    assert convert_to_24_hour("12:00 PM") == "12:00"


if __name__ == "__main__":
    pytest.main()
