'''
Multiprocessor systems at Amazon involve multiple CPUs for performing various tasks,
which increases throughput and reduces response time. A multiprocessor system has a certain number 
of processors.
Each processor has the ability to schedule a limited number of processes in one second. 
However, after each scheduling, the processor's ability is reduced to ability/2 rounded down
to the nearest number. Only one processor can work to schedule processes each second. 
As an Amazonian you are tasked to find the minimum time required to schedule all the processes in the system given the processor's abilities and the number of processes.

Write an algorithm that returns minimum time required to schedule the processes.

Input
The input to the function/method consists of three arguments:
num, an integer representing the number of processors;
ability, a list of integers representing the ability of the processors;
processes, a long integer representing the number of processes to be scheduled.

Output
Return an integer representing the minimum time required to schedule the processes.

Constraints
1 <= num <= 10^5
1 <= ability[i] <= 10^6
1 <= processes <= 10^12
0 <= i < num

Note
It is guaranteed that the processes can be scheduled using the given multiprocessor system.
'''
from collections import heapq
def process_time(num, ability: List[int], processes):
    count = 0
    pq = []
    for abi in ability:
        heapq.heappush(pq, abi)
    
    while processes > 0:
        abi = heapq.heappop(pq)
        processes -= abi
        pq.offer(abi/2)
        count += 1
    return count
    