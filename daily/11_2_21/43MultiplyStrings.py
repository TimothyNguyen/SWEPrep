def multiply_strings(s1, s2):
    ans = 0
    if len(s1) == 0 or len(s2) == 0: return '0'
    if s1[0] == '0' or s2[0] == '0': return '0'

    # convert to integer
    res1, res2 = 0, 0
    for d in range(len(s1)):
        res1 = res1 * 10 + (ord(d) - ord('0'))
    for d in range(len(s2)):
        res2 = res2 * 10 + (ord(d) - ord('0'))

    res = res1 * res2
    return str(res)