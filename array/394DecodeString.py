'''
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
'''
class Solution(object):
    def decodeString(self, s):
        stack, curNum = [], 0
        curString = ''
        for ch in s:
            if ch == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif ch == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + curString * num
            elif ch.isdigit():
                curNum = int(ch)
            else: 
                curString += ch
        return curString
s = '3[a]2[bc]'
ans = Solution().decodeString(s)
print(ans)