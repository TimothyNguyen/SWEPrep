class Solution(object):
    def findDuplicate(self, nums):
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
    
        # Find the "entrance" to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare

'''
fast: 1, 2, 2
slow: 1, 3, 2, 4, 2

1 3 2 4 5
fast: 1, 4, 
slow: 1, 3, 4, 5

slow = tortoise
'''