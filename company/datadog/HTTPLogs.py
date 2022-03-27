'''
You are given the list of logs of HTTP requests in the given format:
[IP, HTTP Verb, status, response time, size, request time]
Write the code to answer the various queries. For example, list all HTTP requests for the last 
2 months or show all requests with 200 status, etc.
Interviewer changes the query structure frequently and you should answer how you are going to attack 
that particular query.
In the end, after the discussion of the pros and cons of different approaches you need to code that.
'''
import collections
from datetime import datetime
from dateutil.relativedelta import relativedelta

def list_logs(arr):
    now = datetime.today()
    past_date = now - relativedelta(months=2)

    # ans = []
    # for elem in arr:
    #     # IP, HTTP_Verb, status, response_time, size, request_time = 
    #     if elem[3] >= past_date or elem[2] == 200:
    #         ans.append(elem)

    # if ordered by date
    # l, r = 0, len(arr)
    # ptr = -1
    # ans = []
    # while l <= r:
    #     m = (l + r) // 2
    #     if arr[m] <= past_date:
    #         l = m + 1
    #     else:
    #         ptr = m
    #         r = m - 1
    # return arr[ptr:] if ptr >= 0 else []

    # Aggregation by status code vs ip addresses
    ans = collections.defaultdict(int)
    for elem in arr:
        ans[elem[2]].append(elem)
    