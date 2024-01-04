import re
import sys
import re


def main():
   print(convert(input("Hours: ")))


def convert(s):
    regex1 = r"\d{1,2}:\d{2} [AP]M to \d{1,2}:\d{2} [AP]M"
    regex2 = r"\d{1,2} [AP]M to \d{1,2} [AP]M"
    if re.match(regex1, s):
        split_s = s.split(" ")
        start_time = split_s[0]
        start_ampm = split_s[1]
        end_time = split_s[3]
        end_ampm = split_s[4]
        start_hr, start_min  = start_time.split(":")
        end_hr, end_min = end_time.split(":")
        start_hr = str (get_24hr(start_hr, start_ampm))
        end_hr = str (get_24hr(end_hr, end_ampm))
    elif re.match(regex2, s):
        split_s = s.split(" ")
        start_hr = split_s[0]
        start_ampm = split_s[1]
        end_hr = split_s[3]
        end_ampm = split_s[4]
        start_min = "00"
        end_min = "00"
        start_hr = str (get_24hr(start_hr, start_ampm))
        end_hr = str (get_24hr(end_hr, end_ampm))
    else:
        exit(1)

    return (f"{start_hr}:{start_min} to {end_hr}:{end_min}")
    

def get_24hr(time, ampm):
    ampm = ampm.lower()
    if ampm == "am":
        if time == 12:
            time = "00"
        else:
            time = "0" + str(time)            
    elif ampm == "pm":
        time = int(time) + 12
    
    return time
    

if __name__ == "__main__":
    main()