import calendar
from datetime import datetime
from datetime import timedelta
import inflect

def main():
    try:
        dob_dt_obj = datetime.strptime(input("Date of birth: "), r'%Y-%m-%d').date()
    except ValueError:
        print("Invalid date")
        exit(1)
    print(convert_dt(dob_dt_obj))


def convert_dt(dob_dt_obj, today_dt_obj=None):
    if today_dt_obj is None:
        today_dt_obj = datetime.today().date()
    delta = today_dt_obj - dob_dt_obj
    minutes = int(delta.total_seconds() / 60)
    words = inflect.engine().number_to_words(minutes)
    return words.capitalize().replace(" and ", " ").strip() + " minutes"


if __name__ == "__main__":
    main()