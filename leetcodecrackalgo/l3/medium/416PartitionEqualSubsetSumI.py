# Given a set of positive numbers, find if we can partition it into 
# two subsets such that the sum of elements in both the subsets is equal.

'''
Example 1: #
Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets 
with equal sum: {1, 4} & {2, 3}
Example 2: #
Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets 
with equal sum: {1, 3, 4} & {1, 7}
Example 3: #
Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets 
with equal sum.
'''

# Time/Space: 0(S*N), where ‘N’ represents total numbers 
# and ‘S’ is the total sum of all the numbers.

class Solution:
    def canPartition(self, num: List[int]) -> bool:
        s = sum(num)

        # if 's' is a an odd number, we can't have two subsets with same total
        if s % 2 != 0:
            return False

        # we are trying to find a subset of given numbers that has a total sum of 's/2'.
        s = int(s / 2)

        n = len(num)
        dp = [[False for x in range(s+1)] for y in range(n)]

        # populate the sum=0 column, as we can always have '0' sum without including 
        # any element
        for i in range(0, n):
            dp[i][0] = True

        # with only one number, we can form a subset only when the required sum is
        # equal to its value
        for j in range(1, s+1):
            dp[0][j] = num[0] == j

        # process all subsets for all sums
        for i in range(1, n):
            for j in range(1, s+1):
              # if we can get the sum 'j' without the number at index 'i'
              if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
              elif j >= num[i]:  # else if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - num[i]]

        # the bottom-right corner will have our answer.
        return dp[n - 1][s]