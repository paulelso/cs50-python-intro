import numb3rs


def main():
    test_validate()
    exit(0)

def test_validate():
    assert numb3rs.validate("127.0.0.1") == True
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("40.247.235.144") == True
    assert numb3rs.validate("256.255.255.255") == False
    assert numb3rs.validate("64.128.256.512") == False
    assert numb3rs.validate("8.8.8") == False
    assert numb3rs.validate("10.10.10.10.10") == False
    assert numb3rs.validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert numb3rs.validate("cat") == False


if __name__ == "__main__":
    main()