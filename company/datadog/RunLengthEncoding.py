'''
Given an input string, write a function that returns the Run 
Length Encoded string for the input string.

For example, if the input string is “wwwwaaadexxxxxx”, then the 
function should return “w4a3d1e1x6”
'''
def cnt(i, prev_s):
    l = i - 1 - prev_s
    cnt_str = ""
    if l > 1:
        cnt_str = str(i - 1 - prev_s)
    return cnt_str

def encode(s):
    if not s or len(s) == 0:
        return ""
    prev_s = 0
    ans = ""
    for i in range(s):
        if s[i] != s[prev_s]:
            ans += cnt(i, prev_s) + s[prev_s]
            prev_s = i
    ans += cnt(i, prev_s) + s[prev_s]