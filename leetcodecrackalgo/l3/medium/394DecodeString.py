'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square 
brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain 
any digits and that digits are only for those repeat numbers, k. For example, there will not be \
input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''
class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def recursive_decode(s):
            nonlocal i
            res = ""
            while i < len(s) and s[i] != ']':
                if not s[i].isdigit():
                    res += s[i]
                    i += 1
                else:
                    k = 0
                    # build k while next char is digit
                    while i < len(s) and s[i].isdigit():
                        k = k * 10 + int(s[i])
                        i += 1
                    i += 1
                    decode_str = recursive_decode(s)
                    i += 1
                    while k > 0:
                        k -= 1
                        res += decode_str
            return res
        return recursive_decode(s)