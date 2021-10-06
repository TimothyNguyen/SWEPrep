'''
Given a set of positive numbers, find if we can partition it into two 
subsets such that the sum of elements in both the subsets is equal.

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two 
subsets with equal sum: {1, 4} & {2, 3}

Time: O(N*S)
'''

# sum: 1-5, index:3=> (dp[index-1][sum] || dp[index-1][sum-4])
def can_partition(nums):
    s = sum(nums)
    if s % 2 != 0:
        return False

    s = s // 2
    dp = [[False for _ in range(s)] for _ in range(len(nums))]
    for i in range(len(dp)):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for j in range(1, s + 1):
        dp[0][j] = nums[0] == j

    # Process all subsets of sum
    for i in range(1, len(nums)):
        for j in range(1, s + 1):
            # if we can get the sum 'j' without the number at index 'i'
            if dp[i - 1][j]:
                dp[i][j] = dp[i-1][j]
            # Else if we can find a subset
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j - nums[i]]
    return dp[len(nums) - 1][s]

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()