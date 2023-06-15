def extra_character_index(str1, str2):
    # Write your code here
    result = 0
    for i in range(len(str1)):
        result = result ^ (ord)(str1[i])
        
    for i in range(len(str2)):
        result = result ^ (ord)(str2[i])

    if len(str1) > len(str2):
        index = str1.index((chr)(result))
        return index
    else:
        index = str2.index((chr)(result))
        return index