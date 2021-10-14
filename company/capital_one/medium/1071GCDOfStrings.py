class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcdVal = gcd(len(str1), len(str2))
        return str2[:gcdVal]
    
    def gcd(p, q):
        if q == 0:
            return p
        return gcd(p%q)
    