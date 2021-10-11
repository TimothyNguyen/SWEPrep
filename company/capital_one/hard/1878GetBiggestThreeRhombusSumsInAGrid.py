'''
You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a 
regular rhombus shape in grid​​​. The rhombus must have the shape of a 
square rotated 45 degrees with each of the corners centered in a 
grid cell. Below is an image of four valid rhombus shapes with the
corresponding colored cells that should be included in each rhombus sum:

Return the biggest three distinct rhombus sums in the grid in descending 
order. If there are less than three distinct values, return all of them.
'''

class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        def calc(l,r,u,d):
            sc=0
            c1=c2=(l+r)//2
            expand=True
            for row in range(u,d+1):
                if c1==c2:
                    sc+=grid[row][c1]
                else:
                    sc+=grid[row][c1]+grid[row][c2]

                if c1==l:
                    expand=False

                if expand:
                    c1-=1
                    c2+=1
                else:
                    c1+=1
                    c2-=1
            return sc


        m=len(grid)
        n=len(grid[0])
        heap=[]
        for i in range(m):
            for j in range(n):
                l=r=j
                d=i
                while l>=0 and r<=n-1 and d<=m-1:
                    sc=calc(l,r,i,d)
                    l-=1
                    r+=1
                    d+=2
                    if len(heap)<3:
                        if sc not in heap:
                            heapq.heappush(heap,sc)
                    else:
                        if sc not in heap and sc>heap[0]:
                            heapq.heappop(heap)
                            heapq.heappush(heap,sc)

        heap.sort(reverse=True)
        return heap