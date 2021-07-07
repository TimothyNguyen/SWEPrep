def longestPalindrome(s):

    def expandAroundCenter(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    if not s or len(s) == 0: return ""
    l, r = 0, 0
    for i in range(len(s)):
        l1 = expandAroundCenter(s, i, i)
        l2 = expandAroundCenter(s, i, i+1)
        m = max(l1, l2)
        if m > r - l:
            l = i - (m - 1) / 2
            r = i + m / 2
    return s[l:r]