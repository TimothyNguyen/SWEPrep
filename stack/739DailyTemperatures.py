class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        ans = [0] * len(temperatures)
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return ans
        
# Example: Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# s = [0] ans = [0,0,0,0,0,0,0,0]
# s = [1] ans = [1,0,0,0,0,0,0,0]
# s = [2] ans = [1,1,0,0,0,0,0,0]
# s = [2, 3] ans = [1,1,0,0,0,0,0,0]
# s = [2, 3, 4] ans = [1,1,0,0,0,0,0,0]
# s = [2,5] ans = [1,1,0,2,1,0,0,0]
# s = [6] ans = [1,1,4,2,1,1,0,0]
# s = [6, 7] ans = [1,1,4,2,1,1,0,0]