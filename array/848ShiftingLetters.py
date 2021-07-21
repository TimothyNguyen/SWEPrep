class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        sum = 0
        for i in shifts: 
            sum += i
        
        res = ""
        for i in range(len(s)):
            L = (ord(s[i])) + (sum % 26)
            #print(sum)
            if 97 <= L <= 122:
                res += chr(L)
            else:
                res += chr(96 + L % 122) 
            sum -= shifts[i]
        return res