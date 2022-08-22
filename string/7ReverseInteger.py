class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >=0:
                revst = strg[::-1]
            else:
                temp = strg[1:]
                temp2 = temp[::-1]
                revst = "-" + temp2
        if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
        return int(revst)