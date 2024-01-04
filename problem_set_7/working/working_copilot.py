import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Check if the input matches either of the expected formats
    if re.match(r"\d{1,2}:\d{2} (AM|PM) to \d{1,2}:\d{2} (AM|PM)", s) or re.match(r"\d{1,2} (AM|PM) to \d{1,2} (AM|PM)", s):
        # Split the input into start and end times
        times = s.split(" to ")
        start_time = times[0]
        end_time = times[1]

        # Convert start time to 24-hour format
        start_time_24 = convert_to_24_hour(start_time)

        # Convert end time to 24-hour format
        end_time_24 = convert_to_24_hour(end_time)

        return f"{start_time_24} to {end_time_24}"
    else:
        raise ValueError("Invalid input format")


def convert_to_24_hour(time):
    # Split the time into hours and minutes
    parts = time.split(":")
    hours = int(parts[0])
    minutes = int(parts[1].split(" ")[0])
    print(hours + minutes)

    # Get the meridiem (AM or PM)
    meridiem = parts[1].split(" ")[1]

    # Handle special cases for 12 AM and 12 PM
    if hours == 12:
        if meridiem == "AM":
            hours = 0
        elif meridiem == "PM":
            hours = 24

    # Adjust hours for PM times
    if meridiem == "PM" and hours != 12:
        hours += 12

    # Check if the time is valid
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        raise ValueError("Invalid time")

    # Format the time as a string in 24-hour format
    return f"{hours:02d}:{minutes:02d}"


if __name__ == "__main__":
    main()
