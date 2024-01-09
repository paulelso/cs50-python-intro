import calendar
from datetime import datetime

def main():
    #dob = input("Date of birth: ")
    s_dob = "2022-12-03"
    dob = datetime.strptime(s, r'%Y-%m-%d').date()
    b_y, b_m, b_d = (dob).strftime('%Y-%m-%d').split("-")
    today = datetime.today().date()
    t_y, t_m, t_d = (today).strftime('%Y-%m-%d').split("-")
    if t_m > b_m:
        print(t_m, b_m)
        print(t_d, b_d)
    print(t_y, t_m, t_d)

    """
    days = 0
    mins = 0
    print(today.year - (dob.year + 1))
    for year in range(dob.year + 1, today.year):
        if is_leap_year(year):
            days = 366
        else:
            days = 365
        mins += days * 24 * 60
    print(mins)
    """

def is_leap_year(year):
    if calendar.isleap(year):
        return True


if __name__ == "__main__":
    main()