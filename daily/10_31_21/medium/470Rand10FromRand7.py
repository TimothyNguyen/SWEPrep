'''
Rejection sampling
- Idea is you generate a number in the desired range, 
output that number immediately. If number is out of 
desired range, reject and re-sample again
# Generate a random integer in the range of 1 to 49
'''
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            r = rand7()
            c = rand7()
            idx = c + (r - 1) * 7
            if idx <= 40:
                break
        return 1 + (idx - 1) % 10
