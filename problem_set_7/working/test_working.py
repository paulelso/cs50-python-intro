import pytest
from working import convert


def test_convert_valid_input():
    assert convert("10:30 AM to 2:45 PM") == "10:30 to 14:45"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"


def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("10:30 AM to 2:45")
    with pytest.raises(ValueError):
        convert("9 AM to 5 PM to 6 PM")
    with pytest.raises(ValueError):
        convert("9:65 AM to 25:01 PM")


def test_convert_to_24_hour():
    assert convert("10:30 AM") == "10:30"
    assert convert("2:45 PM") == "14:45"
    assert convert("12:00 PM") == "12:00"


def test_convert_edge_cases():
    assert convert("12 AM") == "00:00"
    assert convert("12 PM") == "12:00"
    assert convert("11:59 PM") == "23:59"
    assert convert("12:01 AM") == "00:01"


def test_convert_hours_off_by_one():
    assert convert("1:30 AM to 2:45 PM") == "01:30 to 14:45"
    assert convert("9 AM to 6 PM") == "09:00 to 18:00"
    assert convert("11 PM to 1 AM") == "23:00 to 01:00"


def test_convert_minutes_off_by_five():
    assert convert("10:35 AM to 2:45 PM") == "10:35 to 14:45"
    assert convert("9 AM to 5:05 PM") == "09:00 to 17:05"
    assert convert("12 PM to 1:10 PM") == "12:00 to 13:10"


def test_convert_missing_to():
    with pytest.raises(ValueError):
        convert("10:30 AM 2:45 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("12 PM 1 PM")


def test_convert_out_of_range_times():
    with pytest.raises(ValueError):
        convert("-1:30 AM to 2:45 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 25:05 PM")
    with pytest.raises(ValueError):
        convert("12:60 PM to 1:10 PM")


if __name__ == "__main__":
    pytest.main()