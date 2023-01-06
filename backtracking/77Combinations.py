class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        - Have a list to store 1d outputs
        - Have an inner function to backtrack(curr_i, curr_list)
            1. if len(curr_list) == k:
                add to output as a copy
                return
            2. For(i = curr_i -> n+1):
                    add to curr_list(i)
                    backtrack(i + 1, curr_list)
                    remove from curr_list(i)
        '''
        output = []
        def backtrack(curr_i, curr_list):
            if len(curr_list) == k:
                output.append(curr_list[:])
                return
            for i in range(curr_i, n + 1):
                curr_list.append(i)
                backtrack(i + 1, curr_list)
                curr_list.pop()
        backtrack(1, [])
        return output
        