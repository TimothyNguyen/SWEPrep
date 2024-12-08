class Solution:
    num_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(digits, i, curr_result):
            if i == len(digits):
                if curr_result != '':
                    result.append(curr_result)
                return
            digit = digits[i]
            if digit in self.num_to_letters:
                letters = self.num_to_letters[digit]
                for letter in letters:
                    dfs(digits, i + 1, curr_result + letter)

        result = []
        dfs(digits, 0, "")
        return result