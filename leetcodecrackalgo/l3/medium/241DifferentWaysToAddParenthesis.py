'''
Given a string expression of numbers and operators, return all possible results from computing 
all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the 
number of different results does not exceed 104.

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/1294189/Easy-Solution-Faster-than-100-or-Explained-With-Diagrams
'''
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # operations map
        operation = {'*' : lambda x,y: x*y, '+' : lambda x,y: x+y, '-' : lambda x,y: x-y}

        def helper(expression):
            res = []
            for i, x in enumerate(expression):
                if x in ('+', '-', '*'):
                    leftResult = helper(expression[0:i]) # list of results for the left expression(s)
                    rightResult = helper(expression[i+1:]) # list of results for the right expression(s)
                    # append combos
                    for l_val in leftResult:
                        for r_val in rightResult:
                            res.append(operation[x](l_val, r_val))
            # if result list is empty => expression is the single number
            return res if res else [int(expression)]
        return helper(expression)