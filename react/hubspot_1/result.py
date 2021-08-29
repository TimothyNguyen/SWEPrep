# import requests
import json
import datetime
from collections import defaultdict

# OA: For each country, it's required to find two consecutive days, which makes
# the country the largest number of participants.
# Encapsulate the result as json and POST to the second API. When the response code is 500,
# the answer is then correct

def get_data(url=None):
    # Get the data
    #data = requests.get(url)
    #data = data.json()
    f = open('dataset.json')
    return json.load(f)

def is_consecutive(date1, date2):
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    return (date2 - date1).days == 1

def prev_date(date1, date2):
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    return (date1 - date2).days >= 1

def overlap_answer(ans, countries, dates):
    best_day = ''
    attendees = []
    for date in dates:
        if not attendees or len(dates[date]) > len(attendees) or \
            (len(dates[date]) == len(attendees) and prev_date(attendees, dates[date])):
            attendees = dates[date]
            best_day = date
    ans['countries'].append({
        "attendeeCount": len(attendees),
        "attendees": list(attendees),
        "name": countries,
        "startDate": best_day
    })
        

if __name__ == '__main__':
    get_url = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=1cae96d3904b260d06d0daa7387c"
    post_url = "https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=1cae96d3904b260d06d0daa7387c"
    partner_data = get_data()
    countries_dict = dict()
    for person in partner_data['partners']:
        country = person['country']
        if country not in countries_dict:
            countries_dict[country] = []
        countries_dict[country].append(person)

    ans = dict()
    ans['countries'] = list()
    
    dates_dict = defaultdict(set)
    for country in countries_dict:
        for person in countries_dict[country]:
            available_date_list = person['availableDates']
            for i in range(1, len(available_date_list)):
                if is_consecutive(available_date_list[i-1], available_date_list[i]):
                    dates_dict[available_date_list[i - 1]].add(person['email'])

        overlap_answer(ans, country, dates_dict)

    #res = requests.post(post_url, json=ans)
    #ans = (res.status_code, res.content) if res.status_code != 200 else True
    print(ans)
    