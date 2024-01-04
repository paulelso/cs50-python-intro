import re
import sys

s_list = ['9:00 AM to 5:00 PM',
          '12 AM to 11 PM', 
          '9 AM to 5:30 PM', 
          '9:00 AM to 5 PM',
          '9 AM - 5 PM',
          '09:00 AM - 17:00 PM']

regex1 = r'^(0?[1-9]|1[0-2]):[0-5][0-9] AM to (0?[1-9]|1[0-2]):[0-5][0-9] PM$'
s = '11:00 AM to 01:00 PM'
if re.match(regex1, s):
    print("Match")
else:
    print("No match")

