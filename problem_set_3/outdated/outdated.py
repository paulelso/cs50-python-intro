import re

months = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }


def main() -> None:
    prompt_date()


def prompt_date() -> None:
    user_input = input("Date: ").strip()
    # Date format entered 9/8/1636
    if re.match(r'^\d{1,2}/\d{1,2}/\d{4}$', user_input):
        try:
            # Convert the input date to datetime object
            m, d, y = map(int, user_input.split('/'))
        except ValueError:
           main()
        if 0 < d < 32 and 0 < m < 13:
            # Format the date as yyyy-mm-dd
            print(f"{y}-{m:02}-{d:02}")
        else:
             main()
    elif re.match(r'^[A-Za-z]+\s\d{1,2},\s\d{4}$', user_input):
        try:
            m, d, y = re.split(r'\W+', user_input)
            d = int(d)
        except ValueError:
            main()
        if 0 < d < 31 and m in months:
            print(f"{y}-{months[m]:02}-{d:02}")
        else:
            main()
    else:
        main()


if __name__ == "__main__":
    main()