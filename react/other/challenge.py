# import requests
import re
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
  #print(response)
  response_list = list()
  for item in response['results']:
    #print(item['name'], len(item['episode']))
    ans = {
      'name': item['name'],
      'num_episodes': len(item['episode'])
    }
    response_list.append(ans)
  return response_list

# Sort by number of episodes and alphabetical order 
def topCharacters(response, topn):
  response_list = sorted(response, key=lambda x: x['num_episodes'], reverse=True)[:topn]
  response_list = sorted(response_list, key=lambda x: x['name'])
  return response_list

if __name__ == '__main__':
    data = get_data()
    lines = sorted(data['data'], key=lambda k: k['page']['update_time'], reverse=True)
    print(lines)

    main_list = []
    data = main_request(baseurl, endpoint, 1)
    print(data['info']['pages'])
    #print(len(data))
    for x in range(1, get_pages(data) + 1):
      main_list.extend(parse_json(main_request(baseurl, endpoint, x)))

    # data = {"data": main_list} 
    # with open('rickandmorty.json', 'w') as outfile:
    # json.dump(data, outfile)

    #print(len(main_list))
    #df = pd.DataFrame(main_list)
    #print(df.head())
    # df.to_csv('charlist.csv', index=False)

    #with open('rickandmorty.json') as f:
    #  main_list = json.load(f)['data']
    ans = topCharacters(main_list, 20)
    print(ans)

    ans = list(filter((lambda x: 'rick' in x['name'].lower()), ans))
    #print(ans)
    # # ---------- FILTER ----------
    # Filter selects items from a list based on a function
    
    # Print out the even values from a list
    print(list(filter((lambda x: x % 2 == 0), range(1, 20))))