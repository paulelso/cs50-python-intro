import pytest
from datetime import datetime
from seasons import return_words

def test_return_words():
    dob_dt_obj = datetime.strptime("1999-01-01", r'%Y-%m-%d').date()
    today_dt_obj = datetime.strptime("2000-01-01", r'%Y-%m-%d').date()
    assert return_words(dob_dt_obj, today_dt_obj) == "Five hundred twenty-five thousand, six hundred"

    dob_dt_obj = datetime.strptime("2001-01-01", r'%Y-%m-%d').date()
    today_dt_obj = datetime.strptime("2003-01-01", r'%Y-%m-%d').date()
    assert return_words(dob_dt_obj, today_dt_obj) == "One million, fifty-one thousand, two hundred"
    
    dob_dt_obj = datetime.strptime("1995-01-01", r'%Y-%m-%d').date()
    today_dt_obj = datetime.strptime("2000-01-1", r'%Y-%m-%d').date()
    assert return_words(dob_dt_obj, today_dt_obj) == "Two million, six hundred twenty-nine thousand, four hundred forty"

    dob_dt_obj = datetime.strptime("2020-06-01", r'%Y-%m-%d').date()
    today_dt_obj = datetime.strptime("2032-01-01", r'%Y-%m-%d').date()
    assert return_words(dob_dt_obj, today_dt_obj) == "Six million, ninety-two thousand, six hundred forty"

    dob_dt_obj = datetime.strptime("1998-06-20", r'%Y-%m-%d').date()
    today_dt_obj = datetime.strptime("2000-01-01", r'%Y-%m-%d').date()
    assert return_words(dob_dt_obj, today_dt_obj) == "Eight hundred six thousand, four hundred"



    """
   :( Input of "1999-01-01" yields "Five hundred twenty-five thousand, six hundred minutes" when today is 2000-01-01
    Did not find "Five hundred t..." in "Date of birth:..."
:( Input of "2001-01-01" yields "One million, fifty-one thousand, two hundred minutes" when today is 2003-01-01
    Did not find "One million, f..." in "Date of birth:..."
:( Input of "1995-01-01" yields "Two million, six hundred twenty-nine thousand, four hundred forty minutes" when today is 2000-01-1
    Did not find "Two million, s..." in "Date of birth:..."
:( Input of "2020-06-01" yields "Six million, ninety-two thousand, six hundred forty minutes" when today is 2032-01-01
    Did not find "Six million, n..." in "Date of birth:..."
:( Input of "1998-06-20" yields "Eight hundred six thousand, four hundred minutes" when today is 2000-01-01
    Did not find "Eight hundred ..." in "Date of birth:..."
:( Input of "February 6th, 1998" prompts program to exit with sys.exit
    Program exited with a traceback
:( seasons.py passes all checks in test_seasons.py
    expected exit code 0, not 1
    """

if __name__ == "__main__":
    pytest.main()