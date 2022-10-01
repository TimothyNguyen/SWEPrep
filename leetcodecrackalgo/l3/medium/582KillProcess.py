'''
You have n processes forming a rooted tree structure. You are given 
two integer arrays pid and ppid, where pid[i] is the ID of the ith 
process and ppid[i] is the ID of the ith process's parent process.

Each process has only one parent process but may have multiple children 
processes. Only one process has ppid[i] = 0, which means this process
has no parent process (the root of the tree).

When a process is killed, all of its children processes will also be killed.

Given an integer kill representing the ID of a process you want to 
kill, return a list of the IDs of the processes that will be killed. 
You may return the answer in any order.

Example 1:


Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
Output: [5,10]
Explanation: The processes colored in red are the processes that 
should be killed.

Example 2:

Input: pid = [1], ppid = [0], kill = 1
Output: [1]
'''
from collections import defaultdict
from collections import deque

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        ans_dict = defaultdict(set)
        for i in range(len(ppid)):
            ans_dict[ppid[i]].add(pid[i])
            if pid[i] not in ans_dict:
                ans_dict[pid[i]] = set()
        # BFS?
        ans = []
        queue = deque()
        if kill not in ans_dict:
            return ans
        queue.append(kill)
        while queue:
            kill = queue.popleft()
            ans.append(kill)
            for elem in ans_dict[kill]:
                queue.append(elem)
                
        return ans