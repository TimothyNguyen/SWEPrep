class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type arr: List[int]
        :rtype: int
        """
        A = [0]+A
        result = [0]*len(A)
        stack = [0]
        for i in range(1, len(A)):
            #print(i)
            while A[stack[-1]] > A[i]:
                stack.pop() 
            j = stack[-1]
            result[i] = result[j] + (i-j)*A[i]
            stack.append(i)
        return sum(result) % (10**9+7)