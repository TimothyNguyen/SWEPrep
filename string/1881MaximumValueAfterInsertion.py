class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0]=='-':
            for i in range(1,len(n)):
                if x<int(n[i]):
                    return n[:i] + str(x) + n[i:]
        else:
            for i in range(len(n)):
                if x>int(n[i]):
                    return n[:i] + str(x) + n[i:]
        return n + str(x) 