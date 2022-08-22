# class Solution:
#     def letterCombinations(self, digits: str):
#         interpret_digit = {
#             '1': '',
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz',
#             '0': ' '
#         }
        
#         all_combinations = [''] if digits else []
#         for digit in digits:
#             current_combinations = list()
#             for letter in interpret_digit[digit]:
#                 for combination in all_combinations:
#                     current_combinations.append(combination + letter)
#             all_combinations = current_combinations
#         return all_combinations
# s = '23'
# ans = Solution().letterCombinations(s)
# print(ans)

# Time: O(4^N * N)
# Space: O(N)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        interpret_digits = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '
        }
        
        def backtrack(i, path):
            if len(path) == len(digits):
                ans.append("".join(path))
                return
            
            for ch in interpret_digits[digits[i]]:
                path.append(ch)
                backtrack(i+1, path)
                path.pop()
        
        ans = []
        if len(digits) == 0: 
            return ans
        backtrack(0, [])
        return ans