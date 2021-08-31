# import requests
import json
import datetime
from collections import defaultdict
import requests
import pandas as pd

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

def get_data():
    #with open('dataset.json') as json_data:
    #    data_dict = json.load(json_data)
    json_data = open('data.json')
    data_dict = json.load(json_data)
    return data_dict

def to_string(data_dict: dict):
    data_str = json.dumps(data_dict)
    return data_str


# How many episodes is the character in?
def main_request(baseurl, endpoint, x=1):
  r = requests.get(baseurl + endpoint + f'?page={x}')
  return r.json()

def get_pages(response):
  pages = response['info']['pages']
  return pages

def parse_json(response):
  response_list = list()
  for item in response['results']:
    #print(item['name'], len(item['episode']))
    ans = {
      'name': item['name'],
      'num_episodes': len(item['episode'])
    }
    response_list.append(ans)
  return response_list

if __name__ == '__main__':
    data = get_data()
    lines = sorted(data['data'], key=lambda k: k['page']['update_time'], reverse=True)
    print(lines)

    main_list = []
    data = main_request(baseurl, endpoint, 1)
    for x in range(1, get_pages(data) + 1):
        main_list.extend(parse_json(main_request(baseurl, endpoint, x)))

    print(len(main_list))
    #df = pd.DataFrame(main_list)
    #print(df.head())
    # df.to_csv('charlist.csv', index=False)
    

