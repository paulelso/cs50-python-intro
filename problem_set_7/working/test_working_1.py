import pytest
from working import convert


def main():
    test_wrong_format()
    test_wrong_minute()
    test_wrong_hour()
    test_hours_off_by_one()


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")


def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")


def test_hours_off_by_one():
    with pytest.raises(ValueError):
        convert("13 AM to 24 PM")        


if __name__ == "__main__":
    pytest.main()