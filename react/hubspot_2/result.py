# import requests
import json
import datetime
from collections import defaultdict

# OA: Given this input data, we want to create a set of sessions of the incoming data. 
# A sessions is defined as a group of events from a single visitor with no more than 
# 10 minutes between each event. A visitor can have multiple sessions.

def get_data(url=None):
    # Get the data
    #data = requests.get(url)
    #data = data.json()
    f = open('dataset.json')
    return json.load(f)


def get_sessions(ans, visitor_dict):
    sessions = dict()
    for user_id in visitor_dict:
        sessions[user_id] = []
        len_list = len(visitor_dict[user_id])
        
        for idx, val in enumerate(visitor_dict[user_id]):
            if len_list == idx - 1: break
            
        #pages = list(visitor_dict[user_id])
        #for i in range(1, len(pages)):
        #    print(pages[i-1])
        # print(visitor_dict[user_id])
    ans["sessionsByUser"] = sessions

# minutes = (milliseconds/1000)/60
if __name__ == '__main__':
    get_url = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=1cae96d3904b260d06d0daa7387c"
    post_url = "https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=1cae96d3904b260d06d0daa7387c"
    data = get_data()
    visitor_dict = dict()
    for event in data['events']:
        if event['visitorId'] not in visitor_dict:
            visitor_dict[event['visitorId']] = dict()
        timestamp = event['timestamp']
        visitor_dict[event['visitorId']][timestamp] = event['url']
    for user_id in visitor_dict:
        visitor_dict[user_id] = dict(sorted(visitor_dict[user_id].items(), key=lambda item: item[0]))
    ans = dict()
    get_sessions(ans, visitor_dict)
    #print(ans)
    #print(visitor_dict)

