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
        }
        
        ans = []
        
        def backtracking(temp, index):
            if len(digits) == index:
                ans.append(''.join(temp))
                return
            digit = digits[index]
            for letter in interpret_digits[digit]:
                temp.append(letter)
                backtracking(temp, index + 1)
                temp.pop()
        
        if len(digits) == 0:
            return ans
        backtracking([], 0)
        return ans