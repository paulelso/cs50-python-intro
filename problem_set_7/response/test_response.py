import pytest
from response import check_email_validity


def main():
    test_email_validity


def test_email_validity() :
    assert check_email_validity("malan@harvard.edu") == "Valid"
    assert check_email_validity("sysadmins@cs50.harvard.edu") == "Valid"
    assert check_email_validity("malan@harvard") == "Invalid"
    assert check_email_validity("malan.harvard.edu") == "Invalid"
    assert check_email_validity("malan@@@harvard.edu") == "Invalid"
    assert check_email_validity("malan at harvard dot edu") == "Invalid"


if __name__ == "__main__":
    main()