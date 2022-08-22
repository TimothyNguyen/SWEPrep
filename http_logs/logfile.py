# Extract words ["premium grade"], ["Medium grade"]
# 2020-06-30 12:44:11,853 DEBUG [main] [apitests.ApiTest] The Result Obtained from API is : {"keywords": {"Asus Laptop": ["Premium grade"]}}
import re, os
grade = []
dates = []
with open('quality.log', 'r') as f:
    file = f.readlines()
    for line in file:
        # print(line)
        curr_date = re.findall(r'[0-9]{4}-\d{2}-\d{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}', line)
        curr_num_process = re.findall(r'(?<=,)\d{3}', line)
        curr_grade = re.findall(r'\["(.*?)"]', line)
        if curr_grade: grade.append(curr_grade)
        if curr_date: dates.append([curr_date,  curr_num_process])
print(grade) 
print(dates)
# (.*?) is a group containing a non-greedy match.
# (.*)? is an optional group containing a greedy match.

'''
2017-03-18 13:24:05,791 INFO [STDOUT] SUB Request Status :Resubmitted INBIOS_ABZ824


and I need to search the log and extract the values like following,

2017-03-18 13:24:05,791 INBIOS_ABZ824
2017-03-12 13:24:05,796 INDROS_MSR656
2017-04-12 13:24:05,991 INHP_GSN848
'''
# line_regex = 
output_filename = os.path.normpath("output.log")
with open(output_filename, "w") as out_file:
    out_file.write("")

res = []
with open('quality2.log', 'r') as in_f:
    for line in in_f:
        date_time = re.findall(r'\d{4}-\d{2}-\d{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}', line)[0]
        final_word = line.split()[-1]
        res.append(date_time + " " + final_word)
print(res)