class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s1, s2 = dict(), dict()
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in s1 and s[i] not in s2:
                s1[pattern[i]] = s[i]
                s2[s[i]] = pattern[i]
            elif pattern[i] not in s1 or s[i] not in s2:
                return False
            elif s1[pattern[i]] != s[i] or s2[s[i]] != pattern[i]:
                return False
            
        return True