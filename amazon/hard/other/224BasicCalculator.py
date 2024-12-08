class Solution:
    def calculate(self, s: str) -> int:
        s = s.trim()
        ops_stack = []
        num_stack = []
        parenthesis_stack = []
        for i in range(len(s)):
            if s[i] is 