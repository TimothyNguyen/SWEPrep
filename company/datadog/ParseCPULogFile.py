'''
Three columns inside log file generated by single thread CPU, 
assuming input is 
Entry(String jobName, boolean start, int timeStamp), 
output is HashMap<String, List>

write a parse function to parse log file. Please read these 
two examples below very carefully. This problem is more 
complicated than I think !

job (String) start/end (boolean) timestamp (Integer)
f1 true 1
f1 true 2
f2 true 4
f2 false 8
f1 false 16
f1 false 32
f3 true 64
f3 false 128



output: f1: [1,4] [8,32]
f2: [4,8]
f3: [64,128}

Another example:
f1 true 0
f2 true 2
f1 true 5
f1 false 7
f2 false 10
f3 true 11
f3 false 12
f1 false 15
f4 true 16
f4 false 19

Output:
f1: [0,2], [5, 7], [10, 11], [12 15]
f2: [2,5], [7, 10]
f3: [11, 12]
f4: [16, 19]

It seems it is not necessary to compare the peek() value 
from stack, as long as we merge intervals.
Every time it comes to a new LogEntry, we add an interval 
to the current possessed job, and merge the interval if it 
is concatenated with its previous one.

Here are your cases.

A process starts or a process ends.
A process cannot end before it starts.

If a process starts, push it into the stack.
If a process ends, peak the stack.
Compare the function names.

If the names are the same and it isn't ending, 
ignore it. (Could happen with recursive calls, 
but we only care about earliest execution and are using 
the function name not PID to track.)

TRICKY PART
If the element at the top of the stack is the same as the 
current element and its ending, POP the peak from the stack. 
Get the new peak. If there is no peak, return (it's empty) 
else set it's time_stamp to the time_stamp of the current 
element. Why? When a function finishes it's execution, 
it RETURNS. Meaning the previous function in the stack 
(caller) STARTS AGAIN. You need to capture that interval.

Here are my codes:
'''

class Solution:
    def SNAP_JobScheduling(self, fileName):
        '''
        jobMap = {}
        contextStack = []
        curJob = None
        startTime = -1
        f = open(fileName, 'r')
        for line in f:
            jobName, startBool, timeStr = line.split(' ')
            time = int(timeStr)
            if jobName not in jobMap:
                jobMap[jobName] = []
            if curJob == jobName:
                if startBool == 'true':
                    contextStack.append(jobName)
                else:
                    if contextStack:
                        nextJob = contextStack.pop()
                        if nextJob != curJob:
                            jobMap[curJob].append([startTime, time])
                            curJob = nextJob
                            startTime = time
                    else:
                        jobMap[curJob].append([startTime, time])
                        curJob = None
                        startTime = -1
            else:
                if curJob:
                    jobMap[curJob].append([startTime, time])
                    contextStack.append(curJob)
                curJob = jobName
                startTime = time
        return jobMap
        '''
        jobMap = dict()
        context_stack = []
        curJob = None
        startTime = -1
        f = open(fileName, 'r')
        for line in f:
            jobName, startBool, timeStr = line.split(' ')
            time = int(timeStr)
            if jobName not in jobMap:
                jobMap[jobName] = []
            if curJob == jobName:
                if startBool == 'true':
                    context_stack.append(jobName)
                else:
                    if context_stack:
                        nextJob = context_stack.pop()
                        if nextJob != curJob:
                            jobName[curJob].append([startTime, time])
                            curJob = nextJob
                            startTime = time
                        else:
                            jobName[curJob].append([startTime, time])
                            curJob = None
                            startTime = -1
            else:
                if curJob:
                    jobMap[curJob].append([startTime, time])
                    context_stack.append(curJob)
                curJob = jobName
                startTime = time     
'''
f1 true 1
f1 true 2
f2 true 4
f2 false 8
f1 false 16
f1 false 32
f3 true 64
f3 false 128

f1: [1, 4], [8, 32]
f2: [4, 8], 
f3: [64, 128]
'''
