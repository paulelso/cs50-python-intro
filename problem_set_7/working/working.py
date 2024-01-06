import re
import sys


def main():
    print(convert(input("Hours: ")))


def valid_input(s):
    regexs = [
        r"\d{1,2}:\d{2} [AP]M to \d{1,2}:\d{2} [AP]M", # 10:30 AM to 11:30 AM
        r"\d{1,2} [AP]M to \d{1,2} [AP]M", # 10 AM to 11 AM
        r"\d{1,2} [AP]M to \d{1,2}:\d{2} [AP]M", # 10 AM to 11:30 AM
        r"\d{1,2}:\d{2} [AP]M to \d{1,2} [AP]M", # 10:30 AM to 11 AM
    ]
    for regex in regexs:
        if re.match(regex, s):
            return True
       
    return False
    

def convert(s):
    if not valid_input(s):
        raise ValueError(f"Invalid format: {s}")
    times = s.split(" to ")
    start = times[0]
    end = times[1]
    start_24 = convert_to_24hr(start)
    end_24 = convert_to_24hr(end)
    return (f"{start_24} to {end_24}")

def convert_to_24hr(s):
    regex1 = r"\d{1,2}:\d{2} [AP]M" # 10:30 AM
    regex2 = r"\d{1,2} [AP]M" # 10 AM
    if re.match(regex1, s):
        parts = s.split(":")
        hrs = int(parts[0])
        mins = int(parts[1].split(" ")[0])
        meridiem = parts[1].split(" ")[1]    
    elif re.match(regex2, s):
        parts = s.split(" ")
        hrs = int(parts[0])
        mins = 0
        meridiem = parts[1]
    if hrs == 12:
        if meridiem == "AM":
            hrs = 0
        elif meridiem == "PM":
            hrs = 12
    if meridiem == "PM" and hrs != 12:
        hrs += 12
    if hrs < 0 or hrs > 23 or mins < 0 or mins > 59:
        raise ValueError("Invalid time")
    return f"{hrs:02d}:{mins:02d}"


if __name__ == "__main__":
    main()    