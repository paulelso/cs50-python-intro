import pytest
import seasons

def main():
    pass

def test_convert_date_to_minutes():
    assert seasons.convert_date_to_minutes("1990-01-01") == 17894880
    assert seasons.convert_date_to_minutes("2000-12-31") == 12110400

def test_convert_minutes_to_words():
    pass
    assert seasons.convert_minutes_to_words(17894880) == "Seventeen million, eight hundred ninety-four thousand, eight hundred eighty minutes"
    assert seasons.convert_minutes_to_words(12110400) == "Twelve million, one hundred ten thousand, four hundred minutes"

if __name__ == "__main__":
    pytest.main(["-v", "test_seasons.py"])