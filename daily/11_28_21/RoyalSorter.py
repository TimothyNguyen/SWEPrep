# Arranging names in ascending order, firstly by Name and then by roman numerals.

names = ['Louis V', 'Louis VI', 'Louis X', 'Peter I']
temp_ans = []

def sort_names(names):
    res = []
    for i in range(len(names)):
        space_pos = names[i].rindex(" ")
        num = convertToNum(names[i][space_pos + 1:])
        name_val = names[i][:space_pos]
        temp_ans.append([name_val, num, names[i], names[i][space_pos + 1:]])
    temp_ans.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(temp_ans)):
        res.append(temp_ans[i][0] + ' ' + temp_ans[i][2])
    return res
        

def convertToNum(roman_numeral):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total, i = 0, 0
    while i < len(roman_numeral):
        if i + 1 < len(roman_numeral) and values[roman_numeral[i]] < values[roman_numeral[i+1]]:
            total += values[roman_numeral[i + 1]] - values[roman_numeral[i]]
            i += 2
        else:
            total += values[roman_numeral[i]]
            i += 1
    return total

print(sort_names(names))