def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while(stack and temperatures[stack[-1]] < t):
            cur = stack.pop()
            ans[cur] = i - cur
        stack.append(i)
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