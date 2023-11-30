def main():
    time = input("What time is it? ")
    hrs_float = convert(time)
    meal_time = ""
    # breakfast time from 7:00 to 8:00
    if 7.00 <= hrs_float <= 8.00:
        meal_time = "breakfast"
    # lunch time from 12:00 to 13:00
    elif 12.00 <= hrs_float <= 13.00:
        meal_time = "lunch"
    # dinner time from 18:00 to 19:00
    elif 18.00 <= hrs_float <= 19.00:
        meal_time = "dinner"

    if meal_time:
        print(f"{meal_time} time")

# converts time str to the corresponding number of hours as a float.
def convert(time):
    time_exps = time.split(":")
    hrs = float(time_exps[0])
    mins = float(time_exps[1])
    hrs_float = hrs + (mins / 60)

    return hrs_float

if __name__ == "__main__":
    main()