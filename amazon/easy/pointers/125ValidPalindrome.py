class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
        
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()
        if len(new_s) <= 1:
            return True
        l, r = 0, len(new_s) - 1
        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True