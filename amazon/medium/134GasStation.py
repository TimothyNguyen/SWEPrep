class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        curr_tank = 0
        station = 0
        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
            if curr_tank < 0:
                curr_tank = 0
                station = i + 1
        return station if total_tank >= 0 else -1
'''
[1,2,3,4,5]
[3,4,5,1,2]

Total: [-2, -4, -6, -3, 0]
'''