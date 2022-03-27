'''
Given a set of four digit numbers, and two numbers A 
and B which are in the set, indicate if A and B are chainable. 
Any numbers X and Y are chainable if the last two digits of X are 
the first two digits of Y, with any number of chainable numbers in between. 

For example, given the set {8363, 6388, 8183, 5364, 8353, 8365, 9380}, 
A=8183, B=6388, yes, A and B are chainable (as [8183, 8363, 6388]).
'''
import collections
class Solution(object):
    def is_chainable(self, num1, num2, set_numbers):
        if num1 not in set_numbers or num2 not in set_numbers:
            return False
        queue = collections.deque()
        queue.append(str(num1))
        while queue:
            num = queue.popleft()
            if num == str(num2):
                return True
            for elem in set_numbers:
                if num[-2:] == str(elem)[:2]:
                    queue.append(str(elem))
        return False