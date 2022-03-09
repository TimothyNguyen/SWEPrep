class Solution(object):
    def sumSubarrayMins(self, arr):
        arr = [0] + arr
        res = [0] * len(arr)
        stack = [0]
        for i in range(1, len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            res[i] = (i-j)*arr[i] + res[j]
            stack.append(i)
        return sum(res) % (10**9 + 7)
'''
[3, 1, 2, 4]
res = [0, 3, 2*1, 1*2 + 2, 1*4 + 4]
res = [0, 3, 2, 4, 8] -> 17
'''