class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        '''
        0 + 3
        4 + 1
        5 + 3 + 1
        
        First approach - sort by largest to smallest grow times by indices
        
        Let n denote the number of seeds.

        Time complexity: O(nlogn).

        We sort the seeds with O(nlogn) time and iterate it with O(n) time.

        Space complexity: O(n).

        We use O(n) memory for indices and sorting.

        '''
        curr_plant_time = 0
        result = 0
        idx_list = sorted(range(len(plantTime)), key = lambda x: -growTime[x])
        for i in idx_list:
            curr_plant_time += plantTime[i]
            result = max(result, curr_plant_time + growTime[i])
        return result