#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER maxSpan
#

def processLogs(logs, maxSpan):
    # Write your code here
    id_map = dict()
    res = []
    for log in logs:
        log_arr = log.split(" ")
        id, time, label = int(log_arr[0]), int(log_arr[1]), log_arr[2]
        if id not in id_map:
            id_map[id] = time
        elif abs(id_map[id] - time) <= maxSpan:
            res.append(id)
    res.sort()
    for i in range(len(res)):
        res[i] = str(res[i])
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    maxSpan = int(input().strip())

    result = processLogs(logs, maxSpan)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
