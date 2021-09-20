def isEditOneDistanceAway(s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    if abs(m - n) > 1: return False
    counter = 0

    i,  j = 0, 0

    while i < m and j < n:
        if s1[i] != s2[j]:
            if counter == 1: return False
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                i += 1
                j += 1
            counter += 1
        else: # They match
            i += 1
            j += 1
        
    if i < m or j < n:
        counter += 1

    return counter == 1

s1 = "geeks"
s2 = "geets"
print(isEditOneDistanceAway(s1, s2))