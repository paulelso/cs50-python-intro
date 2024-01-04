import re
import sys

s = input("Hours: ")
regex1 = r"\d{1,2}:\d{2} [AP]M to \d{1,2}:\d{2} [AP]M"
regex2 = r"\d{1,2} [AP]M to \d{1,2} [AP]M"
if re.match(regex1, s):
    # Split the input into start and end times
    times = s.split(" to ")
    start_time = times[0]
    end_time = times[1]
    print(f"Start time: {start_time}")
    print(f"End time: {end_time}")
    parts = start_time.split(":")
    print(f"parts: {parts}")
    meridiem = parts[1].split(" ")[1]
    print(f"meridiem: {meridiem}")
    """
elif re.match(regex2, s):
    # Split the input into start and end times
    times = s.split(" to ")
    start_time = times[0]
    end_time = times[1]
    print(f"Start time: {start_time}")
    print(f"End time: {end_time}")
    parts = start_time.split(":")
    print(f"parts: {parts}")
    #meridiem = parts[1].split(" ")[1]
    
   
    hours = int(parts[0])
    minutes = int(parts[1].split(" ")[0])
    print(f"hours: {hours} minutes: {minutes}")
    """