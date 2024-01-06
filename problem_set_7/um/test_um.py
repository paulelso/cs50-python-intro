import pytest
from um import count


def main():
    test_count()    


def test_count():
    assert (count("um\n")) == 1
    assert (count("um?\n")) == 1
    assert (count("Um, thanks for the album.\n")) == 1
    assert (count("Um, thanks, um...\n")) == 2


if __name__ == "__main__":
    main()