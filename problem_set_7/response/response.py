from validator_collection import validators, checkers, errors


def main():
    email = (input("What's your email address? "))
    print(check_email_validity(email))
    

def check_email_validity(email):
    try:
        validators.email(email)
        return "Valid"
    except (errors.EmptyValueError, errors.InvalidEmailError):
        return "Invalid"


if __name__ == "__main__":
    main()