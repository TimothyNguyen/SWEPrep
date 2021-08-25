import requests
import json
import datetime

# OA: For each country, it's required to find two consecutive days, which makes
# the country the largest number of participants.
# Encapsulate the result as json and POST to the second API. When the response code is 500,
# the answer is then correct

def get_country_data(url):
    data = requests.get(url)
    data = data.json()

def post_country_data(url):
    pass

def is_consecutive(date1, date2):
    date1 = datetime.datetime.strptime()