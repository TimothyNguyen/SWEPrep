class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    s = s[0:i] + s[i + 1:]
                    i -= 1
                else:
                    stack.pop()
            i += 1
        moved_idx = 0
        for idx in range(len(stack)):
            i = stack[idx]
            s = s[0:i - moved_idx] + s[i + 1 - moved_idx:]
            moved_idx += 1
        return s