class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds, even = 0, 0
        for elem in position:
            if elem % 2 == 0:
                even += 1
            else:
                odds += 1
        return min(odds, even)
    
# [1, 2, 2, 5] -> output: 2
# [1, 2, 2, 3, 3, 3, 5] -> output: 2
# [1, 4, 6, 6, 7] -> 