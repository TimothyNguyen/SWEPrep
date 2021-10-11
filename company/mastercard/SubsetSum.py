'''
Given a set of positive numbers, determine if there exists a subset 
whose sum is equal to a given number ‘S’.

Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}

Input: {1, 2, 7, 1, 5}, S=10
Output: True
The given set has a subset whose sum is '10': {1, 2, 7}

Input: {1, 3, 4, 8}, S=6
Output: False
The given set does not have any subset whose sum is equal to '6'.

Time: O(N*S)
'''
def can_partition(nums, sum):
    #TODO: Write - Your - Code
    dp = [[False for _ in range(sum + 1)] for _ in range(len(nums))]
    for i in range(len(dp)):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for j in range(1, sum + 1):
        if nums[0] == j:
            dp[0][j] = True
    
    for i in range(1, len(nums)):
        for j in range(1, sum + 1):
            # if upper is true, it's true still
            if dp[i - 1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= nums[i]:
                # else include the number and see if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - nums[i]]
    # the bottom-right corner will have our answer.
    return dp[len(nums) - 1][sum]
'''
def can_partition(num, sum):
    n = len(num)
    dp = [False for x in range(sum+1)]

    # handle sum=0, as we can always have '0' sum with an empty set
    dp[0] = True

    # with only one number, we can have a subset only when the required sum is equal to its value
    for s in range(1, sum+1):
        dp[s] = num[0] == s

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(sum, -1, -1):
            # if dp[s]==true, this means we can get the sum 's' without num[i], hence we can move on to
            # the next number else we can include num[i] and see if we can find a subset to get the
            # remaining sum
            if not dp[s] and s >= num[i]:
                dp[s] = dp[s - num[i]]

    return dp[sum]
'''

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))