# from General Motors HackerRank assessment

import sys
import math

line = input()

# parse input and convert to int as needed
start_time, end_time = line.split('-')
start_h, start_min, start_meridiem = start_time.split()
end_h, end_min, end_meridiem = end_time.split()

start_h, start_min, end_h, end_min = list(map(int, [start_h, start_min, end_h, end_min]))

# account for AM/PM
abs_time = 0
if start_meridiem != end_meridiem:
    abs_time = 12 * 60

# accout for hour difference
abs_time += (end_h - start_h) * 60

# account for minute difference
if end_min - start_min < 0:             # if end minute < start minute,
    abs_time -= (start_min - end_min)   # subtract the time that hasn't yet elapsed to complete the hour
else:
    abs_time += end_min - start_min

# display result
print(abs_time)
        
