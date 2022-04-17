class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        m = defaultdict(int)
        for row in wall:
            total = 0
            for i in range(len(row) - 1):
                total += row[i]
                m[total] += 1
        print(m)
        ans = len(wall)
        for elem in m:
            ans = min(ans, len(wall) - m[elem])
        return ans
            
'''
[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]

{
1: 3
2: 1
3: 3
4: 4
5: 2
6: 0
}
'''