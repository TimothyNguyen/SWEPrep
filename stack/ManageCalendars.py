def merge(meetings):

    res = []
    res.append(meetings[0])
    for i in range(1, len(meetings)):
        if not res[-1][1] < meetings[i][0]:
            res[-1][1] = meetings[i][1]
        else:
            res.append(meetings[i])
    
    return res
        
    
'''
def isAvailable(meetings, start, end):
    
    meetings = [list(i) for i in meetings]
    meetings = sorted(meetings, key = lambda x : x[0])
    meetings = merge(meetings)
    
    if start < meetings[0][0] and end > meetings[-1][1]:
        return False
    
    for i in range(len(meetings)):

        if start == meetings[i][0] and end == meetings[i][1]:
            return False
        
        elif start < meetings[i][0] and end > meetings[i][1]:
            return False
        
        elif meetings[i][0] < start < meetings[i][1] or  meetings[i][0] < end < meetings[i][1]:
            return False
    return True
'''
import heapq
def isAvailable(meetings,start,end):
    hq=[]
    for meeting in meetings:
        heapq.heappush(hq,meeting)
    
    
    x=heapq.heappop(hq)
    
    if x[0]>=  start and end<= x[0]:
        return True
    
    while hq:
  
        if start >= x[1] and end <=hq[0][0]:
          
            return True
        
        
        else:    
            x=heapq.heappop(hq)
            
    if start>=x[1] and end>=x[1]:
        
        return True    
    
    return False     