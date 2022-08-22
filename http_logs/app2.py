from pytz import UTC
from dateutil import parser
import argparse
from lib2to3.pgen2.pgen import generate_grammar
import random
import sched
import time
import sys
import getopt
import random
import os.path
import re
import operator
from datetime import datetime, timedelta, timezone
# from faker import Faker
import pytz as pytz


class LogParser(object):
    def __init__(self, start_time):
        self.start_time = start_time
        self.logs = []
        # self.logs = {}
        self.is_alert = False
        self.alert_logs = []
        self.hits = {}

    def parse_log(self, logString):
        self.rawString = logString
        """
        {
            datetime(2000, 10, 10, 13: 55): {
                "ip_address": "127.0.0.1",
                "user_identifier": "-",
                "requester": "frank",
                "timestamp": datetime(2000, 10, 10, 13, 55, 36),
                "request_method": "GET",
                "resource": "/apache_pb.gif",
                "protocol": "HTTP/1.0",
                "status_code": "200",
                "size": "2326"
            }
        }
        """
        split_line = list(map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', logString)))

        '''
        parsed_line = {
            "ip_address": split_line[0],
            "user_identifier": split_line[1],
            "requester": split_line[2],
            "status_code": split_line[5],
            "size": split_line[6]
        }

        # setting the timestamp
        # parsed_line['timestamp'] = parser.parse(split_line[3].replace(':', ' ', 1)).astimezone(UTC)
        now = datetime.now(timezone.utc)
        parsed_line['timestamp'] = now
        # setting the request method and resource
        split_http = split_line[4].split(" ")
        parsed_line['request_method'] = split_http[0]
        parsed_line['resource'] = split_http[1]
        parsed_line['protocol'] = split_http[2]
        '''

        split_http = split_line[4].split(" ")
        parsed_line = [split_line[0], split_line[1], split_line[2], split_line[5], split_line[6], datetime.now(timezone.utc).replace(microsecond=0), split_http[0], split_http[1], split_http[2]] 

        # adding to a bucketed-by-second dictionary of all logs
        # key_name = str(parsed_line['timestamp'].replace(microsecond=0))
        # print(key_name)
        # print(key_name)

        self.logs.append(parsed_line)

        #if self.logs.get(key_name):
        #    self.logs[key_name].append(parsed_line)
        #else:
        #    self.logs[key_name] = [parsed_line]

        # print(self.logs)
        return parsed_line
    
    def get_logs(self):
        return self.logs

    def most_hits(self):
        """
        `most_hits` goes through the logs list for the time period between now
        and 10 seconds ago and returns:
        (<section that got the most hits>, <how many hits>)
        """
        section_hits = {}
        now = datetime.now(timezone.utc)
        time_key = (now - timedelta(seconds = 10)).replace(microsecond=0)
        l, r = 0, len(self.logs) - 1
        while l <= r:
            m = (l + r) // 2
            if self.logs[m][5] < time_key:
                l = m + 1
            elif self.logs[m][5] > time_key:
                r = m - 1
            else:
                while m > 0 and self.logs[m][5] == time_key:
                    m -= 1
                l = m + 1
                break
        logs = self.logs[l:]
        for log in logs:
            section = log[7].strip('/').split('/', 1)[0]
            if section not in section_hits:
                section_hits[section] = 0
            section_hits[section] += 1
        
        if section_hits != {}:
            # update the overall traffic data store with 10 sec
            for section_name, num_hits in section_hits.items():
                if section_name not in self.hits:
                    self.hits[section_name] = 0
                self.hits[section_name] += num_hits
            section_name = max(section_hits, key=section_hits.get)
            return "/{}".format(section_name), section_hits[section_name]
        return None, None
        '''
        for i in range(0, 10):
            time_key = (now - timedelta(seconds=i)).replace(microsecond=0)
            logs_list = self.logs.get(str(time_key)) or []
            for log in logs_list:
                section = log['resource'].strip('/').split('/', 1)[0]
                if section not in section_hits:
                    section_hits[section] = 0
                section_hits[section] += 1
            
            if section_hits != {}:
                # update the overall traffic data store with 10 sec
                for section_name, num_hits in section_hits.items():
                    if section_name not in self.hits:
                        self.hits[section_name] = 0
                    self.hits[section_name] += num_hits
            section_name = max(section_hits, key=section_hits.get)
            return "/{}".format(section_name), section_hits[section_name]
        return None, None
        '''
    def binary_search_left(self, time_key):
        l, r = 0, len(self.logs) - 1
        while l <= r:
            m = (l + r) // 2
            if self.logs[m][5] < time_key:
                l = m + 1
            elif self.logs[m][5] > time_key:
                r = m - 1
            else:
                while m > 0 and self.logs[m][5] == time_key:
                    m -= 1
                l = m + 1
                break
        return l

    def binary_search_right(self, time_key):
        l, r = 0, len(self.logs) - 1
        while l <= r:
            m = (l + r) // 2
            if self.logs[m][5] < time_key:
                l = m + 1
            elif self.logs[m][5] > time_key:
                r = m - 1
            else:
                while m < len(self.logs) and self.logs[m][5] == time_key:
                    m += 1
                r = m - 1
                break
        return r

    def average_traffic(self, start, seconds):
        """
        `average_traffic` gets the average # of events that happened in the
        past `seconds` amount of seconds from the `start` date time.
        Returns the average traffic.
        """ 
        time_key = (start - timedelta(seconds=seconds)).replace(microsecond=0)
        l = self.binary_search_left(time_key)
        r = self.binary_search_right(start)
        if r < l: return 0
        return (r - l) / seconds
        
        

# python app.py -i logs/alm-log.txt -o access.log -c 1
def printUsage():
    print("Usage: %s -i access_log_input -o access_log_output -c entries" % sys.argv[0])

def writeRandomLogEntries(inFileName, outFileName, entryCount):
    count = entryCount
    now = datetime.now(timezone.utc).astimezone()
    log_parse = LogParser(now)
    while count > 0:
        line = random.choice(open(inFileName).readlines())
        log_parse.parse_log(line)
        count -= 1

    print(log_parse.most_hits())
    start = (datetime.now(timezone.utc).astimezone() - timedelta(seconds=2)).replace(microsecond=0)
    print(log_parse.average_traffic(start, 5))
    print(log_parse.get_logs()[0])

    # ['91.200.12.22', '-', '-', '200', '4494', datetime.datetime(2022, 4, 18, 1, 23, 5, tzinfo=datetime.timezone.utc), 'POST', '/administrator/index.php', 'HTTP/1.1']
    


if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        printUsage()
        sys.exit(2)
    try:
        myopts, args = getopt.getopt(sys.argv[1:], "o:i:c:")
    except getopt.GetoptError as e:
        print (str(e))
        printUsage()
        sys.exit(2)
        
    inFile = None
    outFile = None
    eCount = 1

    for o, a in myopts:
        if o == '-o':
            outFile = a
        elif o == '-i':
            inFile = a
        elif o == '-c':
            eCount = int(a)

    if not os.path.exists(inFile):
        print('Input access_log_input file: %s does not exist' % (inFile))
        sys.exit(2)
    
    writeRandomLogEntries(inFile, outFile, eCount)