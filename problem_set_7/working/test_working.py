import pytest
from working import convert

def main():
    test_convert_to_24hr()
    test_convert_to_24hr_without_to()

def test_convert_to_24hr():
    input_time = "9 AM to 5 PM"
    expected_output = "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    input_time = "9:00 AM to 5:00 PM"
    assert convert(input_time) == expected_output

def test_convert_to_24hr_without_to():
    input_time = "9 AM 5 PM"
    with pytest.raises(ValueError):
        convert(input_time)

def test_convert_to_24hr_out_of_range():
    input_time = "9 AM to 25 PM"
    with pytest.raises(ValueError):
        convert(input_time)


if __name__ == "__main__":
    main()

