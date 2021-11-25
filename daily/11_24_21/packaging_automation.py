# Given a list of items in groups, perform certain operations in order to 
# satisfy the constaints required by packaging automation.

# The conditions are as follows:
# 1. The first group must contain 1 item only.
# 2. For all the other groups, the difference between the number of items in 
# adjacent groups must not be greater than 1. In other words, for 1 <= i <= n, 
# arr[i] - arr[i - 1] <= 1. To accomplish this, the following operations are available:
#   - Rearrange the groups in any way.
#   - Reduce any group to any number that is >= 1.
#
#   Write an algorithm to find the maximum items that can be packaged for the 
#   final group of the list given the conditions above.

# Example - 1 -- arr = [3, 1, 3, 4]. 
# Output: 4. 
# Explanation: Subtract 1 from the first group making the list [2, 1, 3, 4]. 
# Rearrange the list into [1, 2, 3, 4]. The final maximum of items that can be 
# packaged in the last group is 4.

# Example 2 - arr = [1, 1, 1, 1]. Output is 1.
def maxFinial(arr):
    # sort the array in ascending order
    arr.sort()

    # The first element should be 1
    arr[0] = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            arr[i] = arr[i-1] + 1
    return arr[-1]