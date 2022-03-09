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