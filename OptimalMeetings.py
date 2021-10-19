#!/bin/python3

import math
import os
import random
import re
import sys


import datetime
import heapq
#
# Complete the 'find_meeting_slots' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER num_slots
#  2. 2D_STRING_ARRAY employee_schedules
#

def find_meeting_slots(num_slots, employee_schedules):
    # Write your code here
    
    if(len(employee_schedules)) == 0:
        return []
    
    # Get all of the intervals from employee schedule
    all_intervals = [0] * 96 # 24 hours * 4 times (15 min intervals)
    for employee in employee_schedules:
        for list_of_meetings in employee:
            meeting_time = list_of_meetings.split("-")
            start_time, end_time = meeting_time[0], meeting_time[1]
            start_time_list = start_time.split(":")
            start_time_hour, start_time_minute = int(start_time_list[0]), int(start_time_list[1])
            end_time_list = end_time.split(":")
            end_time_hour, end_time_minute = int(end_time_list[0]), int(end_time_list[1])
            
            # Meeting time isn't valid
            #if start_time_minute % 3 != 0 or end_time_minute % 3 != 0 or start_time == end_time:
            #    continue
            
            # Do a two pointer method
            l, r = start_time_hour * 4 + int(start_time_minute / 15), end_time_hour * 4 + int(end_time_minute / 15)
            #print(l)
            #print(r)
            #print(start_time_hour, ":", start_time_minute)
            #print(start_time)
            #print(end_time_hour, ":", end_time_minute)
            #print(end_time)
            while l < r:
                all_intervals[l] += 1
                l += 1
    #print(all_intervals)
    
    min_heap = []
    idx_of_heap = -1
    prev_overlapping_meetings = -1
    start_time = None
    i = 0
    while i < len(all_intervals):
        curr_overlapping_meetings = all_intervals[i]
        if prev_overlapping_meetings != curr_overlapping_meetings:
            time_hour, time_min = int(i / 4), (i % 4) * 15
            if time_hour < 10:
                time_hour = '0' + str(time_hour)
            else:
                time_hour = str(time_hour)
            if time_min == 0:
                time_min = '00'
            else:
                time_min = str(time_min)
            curr_time = time_hour + ':' + time_min
            
            if idx_of_heap != -1:
                min_heap.append((prev_overlapping_meetings, start_time  + '-' + curr_time))
            idx_of_heap += 1
            start_time = curr_time 
            prev_overlapping_meetings = curr_overlapping_meetings
        i += 1
        
    if start_time != '24:00':
        time_hour, time_min = '24', '00'
        curr_time = time_hour + ':' + time_min
        min_heap.append((prev_overlapping_meetings, start_time  + '-' + curr_time))
    min_heap = sorted(min_heap, key = lambda x: (x[0]))
    
    ans = []
    if len(min_heap) < num_slots:
        return ans
    
    i = 0
    while i < num_slots and i < len(min_heap):
        if int(min_heap[i][0]) < len(employee_schedules) - 1:
            ans.append(min_heap[i][1])
        i += 1
    
    if len(ans) != num_slots:
        return []
    ans.sort()
    return ans

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_slots = int(input().strip())

    employee_schedules_rows = int(input().strip())
    employee_schedules_columns = int(input().strip())

    employee_schedules = []

    for _ in range(employee_schedules_rows):
        employee_schedules.append(input().rstrip().split())

    result = find_meeting_slots(num_slots, employee_schedules)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
