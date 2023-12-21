import twttr


def main():
    test_shorten()

def test_shorten():
    assert twttr.shorten("Twitter") == "Twttr"
    assert twttr.shorten("What's your name?") == "Wht's yr nm?"
    assert twttr.shorten("CS50") == "CS50"
    assert twttr.shorten("PYTHON") == "PYTHN"


if __name__ == '__main__':
    main()
