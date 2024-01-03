import bank

def main():
    test_value()

def test_value():
    assert bank.value("hello") == 0, True
    assert bank.value("h") == 20, True
    assert bank.value("HOWDY") == 20, True
    assert bank.value("goodday") == 100, True
    assert bank.value("BONJOUR") == 100, True


if __name__ == '__main__':
    main()