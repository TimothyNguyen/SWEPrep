class Solution:
    roman_char_dict = {
        'I' : 1,
        'IV': 4,
        'V' : 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L' : 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        i = len(s) - 1
        ans = 0
        while i >= 0:
            if i > 0:
                curr_str = s[i-1:i+1]
                if curr_str in self.roman_char_dict:
                    ans += self.roman_char_dict[curr_str]
                    i -= 2
                    continue
            curr_str = s[i]
            if curr_str in self.roman_char_dict:
                ans += self.roman_char_dict[curr_str]
                i -= 1
        return ans

'''
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''